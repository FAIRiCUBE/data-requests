import pystac
import pytest
import os
import json

from typing import Any


def validate_item(item: pystac.item.Item):
    item_is_EDC: bool = False
    # for now exempt edc items from the inventory required fields
    for link in item.links:
        if link.rel == "about" and link.target.startswith("https://collections.eurodatacube.com"):
            item_is_EDC = True
            break

    properties: dict[str, Any] = item.properties

    if not item_is_EDC:
        # validate Data Source
        assert "dataSource" in properties.keys(), "No dataSource in the stac item"
        assert isinstance(properties["dataSource"], str), "dataSource must be a string"
        assert len(properties["dataSource"]) > 0, "dataSource string must not be empty"

        # validate Owner/Organisation
        assert "providers" in properties, "No dataSource in the stac item"
        assert isinstance(properties["providers"], list), "providers must be a list"
        for provider in properties["providers"]:
            assert "organization" in provider.keys() or "name" in provider.keys()
            if "organization" in provider.keys():
                assert isinstance(provider["organization"], str), "provider's organization must be a string"
                assert len(provider["organization"]) > 0, " provider's organization must not be empty"
            if "name" in provider.keys():
                assert isinstance(provider["name"], str), "provider name must be a string"
                assert len(provider["name"]) > 0, "provider name string must not be empty"

        # validate Horizontal section
        assert isinstance(item.bbox, list), "bbox must be a list"
        assert len(item.bbox) == 4, "bbox must contain a 4 coordinates"
        assert isinstance(item.geometry, dict),"geometry must be an object"

        # Resolution of Horizontal Axis
        assert isinstance(item.properties["cube:dimensions"], dict), "No dimensions in the stac item"
        assert "x" in item.properties["cube:dimensions"].keys(), "No x dimension in the stac item"
        assert "y" in item.properties["cube:dimensions"].keys(), "No y dimension in the stac item"
        x = item.properties["cube:dimensions"]["x"]
        y = item.properties["cube:dimensions"]["y"]
        assert "step" in x.keys() and x["step"] is not None, "No step in the x  dimension"
        assert isinstance(float(x["step"]), float), "x step must be float"
        assert "step" in y.keys()and y["step"] is not None, "No step in the x  dimension"
        assert isinstance(float(y["step"]), float), "y step must be float"

        # Units of Measurement
        assert "unit" in x.keys(), "No unit in x dimensions"
        assert isinstance(x["unit"], str), "x dimension unit must be a string"
        assert "unit" in y.keys(), "No unit in y dimensions"
        assert isinstance(y["unit"], str), "y dimension unit must be a string"

        # Horizontal CRS
        assert "reference_system" in x.keys(), "No reference_system in x dimensions"
        assert isinstance(x["reference_system"], str), "x dimension reference_system must be a string"
        assert "reference_system" in y.keys(), "No reference_system in y dimensions"
        assert isinstance(y["reference_system"], str), "x dimension reference_system must be a string"

        # Temporal
        assert "t" in item.properties["cube:dimensions"].keys() or "time" in item.properties["cube:dimensions"].keys()
        time = dict()
        if "t" in item.properties["cube:dimensions"].keys():
            time = item.properties["cube:dimensions"]["t"]
        else:
            time = item.properties["cube:dimensions"]["time"]

        # Time (Begin/End)
        assert "extent" in time.keys() or "values" in time.keys()
        # Resolution of Time Axis (Interval)
        if "extent" in time.keys():
            assert "step" in time.keys(), "No step in time dimensions"
            assert isinstance(time["step"], str), "time's step must be a string"
        # Unit of measure
        assert "unit" in time.keys(), "No unit in time dimensions"
        assert isinstance(time["unit"], str), "time's unit must be a string"


        # Range Data validation
        assert "raster:bands" in item.properties.keys() or "bands" in item.properties.keys()
        #TODO figure out a way to validate edc items , the ones with "bands"

        if "raster:bands" in item.properties.keys():
            bands = item.properties["raster:bands"]
            assert len(bands) > 0, "bands list must not be empty"
            for band in bands:
                # Range Data Type
                assert "data_type" in band.keys(), "No data_type in band"
                assert isinstance(band["data_type"], str), "band's data_type must be a string"
                assert len(band["data_type"]) > 0, "band's data_type string must not be empty"

                # Range Definition
                assert "definition" in band.keys(), "No definition in band"
                assert isinstance(band["definition"], str), "band's definition must be a string"
                assert len(band["definition"]) > 0, "band's definition string must not be empty"

                # Range Description
                assert "description" in band.keys(), "No description in band"
                assert isinstance(band["description"], str), "band's description must be a string"
                assert len(band["description"]) > 0, "band's description string must not be empty"

                # Null values

                assert "nodata" in band.keys() and band["nodata"]is not None, "No nodata in band"
                assert isinstance(float(band["nodata"]), float), "band's nodata must be float"



    # validate ID
    assert isinstance(item.id, str), "id must be a string"

    assert len(item.id) > 0, "item id string must not be empty"


    # validate Description
    assert "description" in properties.keys(), "No description in the stac item"
    assert isinstance(properties["description"], str), "description must be a string"
    assert len(properties["description"]) > 0, "description string must not be empty"


    # Legal - License
    assert "license" in item.properties.keys(), "No license in the stac item"
    assert isinstance(item.properties["license"], str), "license must be a string"

    #TODO: keywords must be a list
    # Keywords
    assert "keywords" in item.properties.keys(), "No keywords in the stac item"
    keywords = item.properties["keywords"]
    assert isinstance(keywords, list) or (isinstance(keywords, str) and isinstance(keywords.split(","), list)), "keywords is not a valid list"
    assert len(item.properties["keywords"]) > 0, "keywords must not be empty"

@pytest.mark.parametrize("dir", [
        os.path.join('stac_dist', f) for f in os.listdir(
            os.path.join('stac_dist')) if os.path.isdir(os.path.join('stac_dist', f))])
def test_items(dir):

    items = [
        f for f in os.listdir(dir) if not f.endswith(
            'catalog.json') and f.endswith('.json')]

    for item in items:
        item_path = os.path.join(dir, item)

        stac_item = pystac.Item.from_file(item_path)

        validate_item(stac_item)



# In addition, some fields can be filled with defaults, e.g.
# Metadata Standard: STAC
# Provision Date: Date being provided