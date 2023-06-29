from datetime import datetime
import re
import pystac
from pystac.extensions import datacube
from shapely.geometry import Polygon, mapping
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport


GH_TOKEN = "<github-token>"

pystac.set_stac_version("2.2.0")


def create_axes(axes):
    start_date = datetime.strptime("1990-01-01T00:00:00Z", "%Y-%m-%dT%H:%M:%SZ")
    end_date = datetime.strptime("2023-01-01T00:00:00Z", "%Y-%m-%dT%H:%M:%SZ")
    bbox = [[-180.0, -90.0, 180.0, 90.0]]
    footprint = Polygon(
            [
                [-180.0, -90.0],
                [-180.0, 90.0],
                [180.0, 90.0],
                [180.0, -90.0],
            ]
    )
    return start_date, end_date, bbox, mapping(footprint)


def create_links(title):
    self_href = f"https://fairicube.github.io/data-requests/{title}.json"
    root_href = "https://fairicube.github.io/data-requests/index.json"
    self_link = pystac.Link(
        rel="self",
        media_type="application/json",
        target=self_href
    )
    root_link = pystac.Link(
        rel=pystac.RelType("root"),
        media_type=pystac.MediaType("application/json"),
        target=root_href
    )
    parent_link = pystac.Link(
        rel=pystac.RelType("parent"),
        media_type=pystac.MediaType("application/json"),
        target=root_href
    )
    return [self_link, root_link, parent_link]


def create_stac_item(doc, title):

    start_date, end_date, bbox, footprint = create_axes(doc)

    properties = dict()
    # properties["license"] = doc["License"]

    extensions = [
        "https://stac-extensions.github.io/datacube/v2.0.0/schema.json",
        "https://stac-extensions.github.io/raster/v2.0.0/schema.json"
    ]
    links = create_links(title)
    if "ID" in doc.keys():
        id = doc["ID"].replace(" ", "_")
    else:
        id = title
    stac_item = pystac.Item(
        id=id,
        stac_extensions=extensions,
        datetime=datetime.strptime("2000-01-01T00:00:00Z", "%Y-%m-%dT%H:%M:%SZ"),
        bbox=bbox,
        geometry=footprint,
        properties=properties,
    )

    stac_item.links = links
    item_datacube = datacube.DatacubeExtension.ext(stac_item)
    dimensions = dict()
    x_dimension = datacube.HorizontalSpatialDimension({
        "axis": datacube.HorizontalSpatialDimensionAxis("x"),
        "extent": [-180, 180],
        "reference_system": "ESPG:4326",


        })
    y_dimension = datacube.HorizontalSpatialDimension({
        "axis": datacube.HorizontalSpatialDimensionAxis("y"),
        "extent": [-90, 90],
        "reference_system": "ESPG:4326",


    })
    temporal_deminsion = datacube.TemporalDimension({
        "values": [
            datetime.strptime(
                "2000-01-01T00:00:00Z", "%Y-%m-%dT%H:%M:%SZ").isoformat()
            ]

    })
    dimensions["x"] = x_dimension
    dimensions["y"] = y_dimension
    dimensions["time"] = temporal_deminsion

    item_datacube.dimensions = dimensions

    return stac_item


def validate_document(document):
    keys = [
        "ID", "Description", "Project purpose",
        "Preferred Platform", "Preferred Method", "Axes", "Cell type",
        "Null values", "(Meta) data Standards", "APIs", "Access control",
        "Responsible", "Data Source", "Data Preprocessing", "Quality Control",
        "Documents & publications", "License", "Ownership", "Personal Data",
        "Additional Information"
    ]
    document_keys = list(document.keys())

    return keys == document_keys or set(
        document_keys) - set(keys) == {"Target Platform"}


def insert_value(field, value_list, listed_fields, doc):

    if field in listed_fields:
        if len(value_list) == 1:
            doc[field] = value_list[0].split(", ")
        else:
            doc[field] = value_list
    else:
        doc[field] = "\n".join(value_list)


transport = RequestsHTTPTransport(
    url="https://api.github.com/graphql",
    headers={"Authorization": "token " + GH_TOKEN})

client = Client(transport=transport)

query_1 = gql(
        """
        query  {
            organization(login: "FAIRiCUBE") {
                repository(name: "data-requests") {
                    issues(last:100, states:OPEN) {
                        edges {
                            node {
                            title
                            body
                            projectItems(first:10) {
                              edges {
                                node {
                                id
                                fieldValues(first:30) {
                                    nodes {
                                        ... on ProjectV2ItemFieldTextValue {
                                            text
                                            field{
                                                ... on ProjectV2Field {
                                                    name
                                                }
                                            }
                                        }
                                        ... on ProjectV2ItemFieldNumberValue {
                                            number
                                            field{
                                                ... on ProjectV2Field {
                                                    name
                                                }
                                            }
                                        }
                                    }
                                }
                              }
                            }
                            }
                        }
                        }
                    }
                }
            }
        }
        """
    )

issues = client.execute(query_1)[
    "organization"]["repository"]["issues"]["edges"]
index_catalog = pystac.Catalog.from_file('../index.json')
for index, issue in enumerate(issues):
    title = issue["node"]["title"].split("]: ")[-1].replace(" ", "_")
    issue_type = re.findall(r'\[(.*?)\]', issue["node"]["title"])

    project_item = next(iter(issue['node']['projectItems']['edges']), None)

    if project_item:
        fields = project_item['node']['fieldValues']['nodes']
        doc = dict()
        for field in fields:
            if "text" in field.keys():
                doc[field["field"]["name"]] = field["text"]
            elif "number" in field.keys():
                doc[field["field"]["name"]] = field["number"]
        stac_item = create_stac_item(doc, title)
        index_catalog.add_item(stac_item)

    elif next(iter(issue_type), None) == "Data Request":

        input_txt = issue["node"]["body"]
        values = []
        document = dict()
        temp_values = []
        list_fields = ["APIs", "Null values", "(Meta) data Standards"]

        response_lines = input_txt.splitlines()
        fields = []
        for index, i in enumerate(response_lines):

            if i != "\n" and i != "":
                st = i.strip("\n")
                st = st.strip(" ")
                st = st.replace("'", "")
                values.append(st)
        field = ""
        for index, value in enumerate(values):
            if type(value) == str and value.startswith("### "):

                field = values[index][4:]
                fields.append(field)

                if len(temp_values) > 0:
                    temp_values = []
                    fields.pop(0)
            else:
                value = value.replace("_No response_", "")
                temp_values.append(value)

            if index == len(values) - 1:
                document[field] = temp_values

            insert_value(field, temp_values, list_fields, document)
        if validate_document(document):

            stac_item = create_stac_item(document, title)
            index_catalog.add_item(stac_item)

        index_catalog.normalize_and_save(
                root_href="https://fairicube.github.io/data-requests/stac/",
                catalog_type=pystac.CatalogType.ABSOLUTE_PUBLISHED)
