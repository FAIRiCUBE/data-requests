import pystac
import pytest
import os
from typing import Any


def validate_item(item: pystac.item.Item):
    properties: dict[str, Any] = item.properties

    # validate ID
    assert isinstance(item.id, str)

    assert len(item.id) > 0

    # validate Description
    assert "description" in properties.keys()

    # assert isinstance(properties["description"], str)
    # assert len(properties["description"]) > 0


@pytest.mark.parametrize("dir", [
        os.path.join('stac_dist', f) for f in os.listdir(
            os.path.join('stac_dist')) if os.path.isdir(os.path.join('stac_dist', f))])
def test_items(dir):

    items = [
        f for f in os.listdir(dir) if not f.endswith(
            'catalog.json') and f.endswith('.json')]

    for item in items:
        stac_item = pystac.Item.from_file(os.path.join(dir, item))
        validate_item(stac_item)



# Mandatory Columns (additions in bold)
# ID [Column C]
# Description [D]
# Data Source [Column E]
# Owner/Organisation [G]
# Horizontal
# Horizontal CRS [Column P]
# Bounding Box (Horizontal) [Column Q-T]
# Resolution of Horizontal Axis (ie. Pixel Size) [Column W]
# Units of Measurement [Column U]
# Temporal
# Time (Begin/End) [Column AD-AE]
# Resolution of Time Axis (Intervall) [Column AH]
# Unit of measure [Column AF]
# Range Data Type [Column AR]
# Range Definition [AS]
# Range Description [AT]
# Null values [Column AQ]
# Legal - License [BA]
# Keywords - Keywords [BJ]
# In addition, some fields can be filled with defaults, e.g.
# Metadata Standard: STAC
# Provision Date: Date being provided