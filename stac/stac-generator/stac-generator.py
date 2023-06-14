
import json
from datetime import datetime
import pystac
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport


GH_TOKEN = "<github-token>"


def create_axes(axes):
    start_date = datetime.strptime("1990-01-01T00:00:00Z", "%Y-%m-%dT%H:%M:%SZ")
    end_date = datetime.strptime("2023-01-01T00:00:00Z", "%Y-%m-%dT%H:%M:%SZ")
    spatial_extent = pystac.SpatialExtent(bboxes=[[-180.0, -90.0, 180.0, 90.0]])
    temporal_extent = pystac.TemporalExtent(intervals=[[
                start_date, end_date
                ]])
    return pystac.Extent(spatial=spatial_extent, temporal=temporal_extent)


def create_stac_collection(doc, title):


    collection_extent = create_axes(doc["Axes"])

    extensions = [
        "https://stac-extensions.github.io/datacube/v1.0.0/schema.json",
        "https://stac-extensions.github.io/raster/v1.0.0/schema.json"
    ]

    collection = pystac.Collection(
        id=doc["ID"],
        title=title,
        description=doc["Description"],
        stac_extensions=extensions,
        extent=collection_extent,
        license=doc["License"]
    )

    return collection


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

    return keys == document_keys or set(document_keys) - set(keys) == {"Target Platform"}


def insert_value(field, value_list, listed_fields, doc):

    if field in listed_fields:
        if len(value_list) == 1:
            doc[field] = value_list[0].split(", ")
        else:
            doc[field] = value_list
    else:
        doc[field] = "\n".join(value_list)


def stac_builder(input_txt, title):

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

        collection = create_stac_collection(document, title)
        out_stac = f"../{title}.json"
        with open(out_stac, 'w') as file:
            json.dump(collection.to_dict(), file, indent=4)
        file.close()




transport = RequestsHTTPTransport(
    url="https://api.github.com/graphql",
    headers={"Authorization": "token " + GH_TOKEN})

client = Client(transport=transport)

query_1 = gql(
        """
        query  {
            organization(login: \"FAIRiCUBE\") {
                repository(name: "data-requests") {
                    issues(last:100, states:OPEN) {
                        edges {
                            node {
                            title
                            body
                            }
                        }
                        }
                    }
                }
            }
        """
    )

issues = client.execute(query_1)["organization"]["repository"]["issues"]["edges"]
for index, issue in enumerate(issues):
    title = issue["node"]["title"].split("]: ")[-1]
    stac_builder(issue["node"]["body"], title)
