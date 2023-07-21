import requests
from datetime import datetime
from shapely.geometry import Polygon, mapping
import pystac

from pystac.extensions import datacube


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


catalog_url = "https://collections.eurodatacube.com/stac/index.json"
index_collection = requests.get(catalog_url).json()
index_catalog = pystac.Catalog(
        id="index",
        title="data-access catalog",
        description="The stac catalog that contains all the generated datacube items."
    )

for item in index_collection:

    col = requests.get(item["link"]).json()
    collection = pystac.Collection.from_dict(col)
    extent = collection.extent.to_dict()

    bbox = extent["spatial"]["bbox"][0]

    footprint = Polygon(
            [
                [bbox[0], bbox[1]],
                [bbox[0], bbox[3]],
                [bbox[2], bbox[3]],
                [bbox[2], bbox[1]],
            ]
    )

    date = extent["temporal"]["interval"][0][0]
    if date is None:
        date = '2000-01-01T00:00:00Z'
    extra_fields = dict()
    for field in collection.extra_fields:
        if field not in ["type", "cube:dimensions"]:
            extra_fields[field] = collection.extra_fields[field]

    extra_fields.update(collection.summaries.to_dict())
    providers_list = []
    providers = collection.providers
    for provider in providers:
        providers_list.append(provider.to_dict())

    extra_fields["providers"] = providers_list
    extra_fields["description"] = collection.description
    extra_fields["keywords"] = collection.keywords
    extra_fields["title"] = collection.title
    extra_fields["license"] = collection.license

    versioned_ext = collection.stac_extensions
    v1_schema = 'https://stac-extensions.github.io/datacube/v1.0.0/schema.json'
    if v1_schema in versioned_ext:
        versioned_ext.remove(v1_schema)
    versioned_ext.append('https://stac-extensions.github.io/datacube/v2.0.0/schema.json')

    feature = pystac.Item(
        id=collection.id,
        stac_extensions=versioned_ext,
        datetime=datetime.strptime(date, "%Y-%m-%dT%H:%M:%SZ"),
        bbox=bbox,
        geometry=mapping(footprint),
        properties=dict(),
        assets=collection.assets
    )
    dimension_object = collection.extra_fields["cube:dimensions"]
    dims = dict()
    for dim in dimension_object.keys():

        dimension = pystac.extensions.datacube.Dimension.from_dict(dimension_object[dim])

        dims[dim] = dimension

    item_datacube = datacube.DatacubeExtension.ext(feature)

    item_datacube.dimensions = dims
    feature.extra_fields = extra_fields
    collection_links = collection.links
    for link in collection_links:
        if link.rel == "self" or (link.rel == "license" and link.href == ''):
            collection_links.remove(link)
    additional_links = create_links(feature.id)
    collection_links.extend(additional_links)

    feature.links = collection_links

    index_catalog.add_item(feature)

index_catalog.normalize_and_save(
        root_href="stac_dist/",
        catalog_type=pystac.CatalogType.SELF_CONTAINED,
        skip_unresolved=True)
