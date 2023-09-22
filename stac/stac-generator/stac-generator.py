import os
import json
from datetime import datetime
import re
import pystac
from pystac.extensions import datacube
from shapely.geometry import Polygon, mapping
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

GH_TOKEN = os.environ["GH_TOKEN"]

pystac.set_stac_version("2.2.0")


def extract_value_from_string(pattern, string, default):
    match = re.search(pattern, string)
    if match is not None:
        return match.group()
    else:
        return default


def create_axes(axes):
    start = None
    end = None
    edges = [-180.0, -90.0, 180.0, 90.0]
    crs = "EPSG:4326"

    if "Spatial axis" in axes.keys():

        dims = axes["Spatial axis"].split('\n')
        extent_match = re.search(r'\[(.*?)\]', dims[0])

        if extent_match is not None:
            edges = json.loads(extent_match.group(0))
        if len(dims) >= 2:
            crs_match = re.match(r"spatial reference\s*:\s*(.*)", dims[1])
            if crs_match:
                crs = crs_match.group(1)

    if "Time" in axes.keys():
        times = axes["Time"].split('\n')
        start = extract_value_from_string(r'\d{4}-\d{2}-\d{2}', times[0], "1990-01-01")
        if len(times) >= 2:
            end = extract_value_from_string(r'\d{4}-\d{2}-\d{2}', times[1], "2023-01-01")
    if start and end:
        start_date = datetime.strptime(start, "%Y-%m-%d").isoformat()

        end_date = datetime.strptime(end, "%Y-%m-%d").isoformat()
    else:
        start_date = None
        end_date = None
    bbox = edges
    footprint = Polygon(
            [
                [edges[0], edges[1]],
                [edges[0], edges[3]],
                [edges[2], edges[3]],
                [edges[2], edges[1]],
            ]
    )
    return start_date, end_date, bbox, mapping(footprint), crs


def create_links(title):
    self_href = f"https://fairicube.github.io/data-requests/{title}.json"
    root_href = "https://fairicube.github.io/data-requests/catalog.json"
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


def create_assets(doc):
    assets = dict()
    if "APIs" in doc.keys():
        for index, api in enumerate(doc["APIs"]):
            regex = r'^https?://[A-Za-z0-9./?&%=_%]+$'
            match = re.search(regex, api)
            if match is not None and match.span() == (0, len(api)):
                asset = pystac.Asset(
                    roles=["data"],
                    href=match.group(0)

                )
                assets[f"data_{index + 1}"] = asset

    return assets


def create_stac_item(doc, title):

    start_date, end_date, bbox, footprint, crs = create_axes(doc)
    assets = create_assets(doc)

    properties = dict()
    providers = []
    extensions = [
        "https://stac-extensions.github.io/datacube/v2.0.0/schema.json"
    ]
    links = create_links(title)
    if "ID" in doc.keys():
        spaceless_id = doc["ID"].replace(" ", "_")
        id = spaceless_id.replace("–", "_")
        properties["license"] = doc["License"]
        properties["Description"] = doc["Description"]
        providers_list = doc["Ownership"].split(',')
        for provider in providers_list:
            new_provider = pystac.Provider(name=provider)
            providers.append(new_provider.to_dict())
        properties["providers"] = providers
        properties["Data Source"] = doc["Data Source"]

        if "Thumbnails" in doc.keys():
            thumbnails = doc["Thumbnails"]
            if type(doc["Thumbnails"]) != list:
                thumbnails = [doc["Thumbnails"]]
            for index, thumbnail in enumerate(thumbnails):
                asset = pystac.Asset(
                    roles=["thumbnail"],
                    href=thumbnail,
                )
                assets[f"thumbnail_{index}"] = asset
    else:
        id = title
    stac_item = pystac.Item(
        id=id,
        stac_extensions=extensions,
        datetime=datetime.strptime("2000-01-01T00:00:00Z", "%Y-%m-%dT%H:%M:%SZ"),
        bbox=bbox,
        geometry=footprint,
        properties=properties,
        assets=None if len(assets) == 0 else assets
    )

    stac_item.links = links
    item_datacube = datacube.DatacubeExtension.ext(stac_item)
    dimensions = dict()
    x_dimension = datacube.HorizontalSpatialDimension({
        "axis": datacube.HorizontalSpatialDimensionAxis("x"),
        "extent": [bbox[0], bbox[2]],
        "reference_system": "ESPG:4326",
        "type": "spatial"

        })
    y_dimension = datacube.HorizontalSpatialDimension({
        "axis": datacube.HorizontalSpatialDimensionAxis("y"),
        "extent": [bbox[1], bbox[3]],
        "reference_system": "ESPG:4326",
        "type": "spatial"

    })
    if start_date and end_date:
        temporal_dimension = datacube.TemporalDimension({
            "extent": [start_date, end_date],
            "type": "temporal"

        })

    else:

        temporal_dimension = datacube.TemporalDimension({
            "values": [
                datetime.strptime(
                    "2000-01-01T00:00:00Z", "%Y-%m-%dT%H:%M:%SZ").isoformat()
                ],
            "type": "temporal"

        })
    dimensions["x"] = x_dimension
    dimensions["y"] = y_dimension
    dimensions["time"] = temporal_dimension

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
                            labels(first:10) {
                            edges {
                                node {
                                name
                                }
                            }
                            }
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
# index_catalog = pystac.Catalog(
#     id="index",
#     title="data-access catalog",
#     description="The stac catalog that contains all the generated datacube items."
# )
index_catalog = pystac.Catalog.from_file('./stac_dist/catalog.json')
for index, issue in enumerate(issues):
    labels = issue["node"]["labels"]["edges"]
    requested = {'node': {'name': 'data-request'}}
    if requested in labels:

        title = issue["node"]["title"].split("]: ")[-1].replace(" ", "_")
        title = title.replace("–", "_")
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

            # if validate_document(document):

            stac_item = create_stac_item(document, title)
            index_catalog.add_item(stac_item)

    index_catalog.normalize_and_save(
            root_href="stac_dist/",
            catalog_type=pystac.CatalogType.SELF_CONTAINED)
