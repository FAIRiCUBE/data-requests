import os
import pystac


# update catalogs

directories = [
    os.path.join('stac_dist', f) for f in os.listdir(
        os.path.join('stac_dist')) if os.path.isdir(os.path.join('stac_dist', f))]
catalog = pystac.Catalog.from_file(os.path.join('stac_dist', 'catalog.json'))
catalog.clear_items()
for dir in directories:
    items = [
        f for f in os.listdir(dir) if not f.endswith(
            'catalog.json') and f.endswith('.json')]

    for item in items:
        stac_item = pystac.Item.from_file(os.path.join(dir, item))
        catalog.add_item(stac_item)

catalog.save(
    catalog_type=pystac.CatalogType.SELF_CONTAINED
)
