import requests
import os
import pystac
from requests.auth import HTTPBasicAuth

username = os.environ["USERNAME"]
password = os.environ["PASSWORD"]

catalog_url = "https://fairicube.github.io/data-requests/catalog.json"
post_url = "https://stacapi-write.eoxhub.fairicube.eu/collections/index/items"


def delete_item(id):
    response = requests.delete(url=f"{post_url}/{id}",
                               auth=HTTPBasicAuth(username, password))
    return response.status_code


index_catalog = requests.get(catalog_url).json()
catalog = pystac.Catalog.from_dict(index_catalog)
catalog_items = catalog.get_items()

catalog_items_list = []

for item in catalog_items:
    catalog_items_list.append(item.id)

api_items = requests.get(url=f"{post_url}?limit=1000",
                         auth=HTTPBasicAuth(username, password)).json()

# check if the already ingested items are in the catalog, otherwise delete them
for item in api_items["features"]:
    if item["id"] not in catalog_items_list:
        delete_item(item["id"])

for link in index_catalog["links"]:
    if link["rel"] == "item":
        json_body = requests.get(link["href"]).json()
        response = requests.post(
            url=post_url, json=json_body,
            auth=HTTPBasicAuth(
                username, password))
        if response.status_code == 409:
            put_url = f'{post_url}/{json_body["id"]}'
            response = requests.put(
                url=put_url, json=json_body,
                auth=HTTPBasicAuth(
                    username, password))
        print(response, json_body["id"])
