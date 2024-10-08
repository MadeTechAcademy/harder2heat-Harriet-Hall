import pytest
import json
import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from src.property import Property

with open("./properties.json", "r") as data:
    dummy_data = json.load(data)
    dummy_data_property = dummy_data[0]["properties"]


@pytest.fixture
def dummy_property():
    uprn = dummy_data_property["uprnreference"][0]["uprn"]
    year = dummy_data_property["buildingage_year"]
    connectivity = dummy_data_property["connectivity"]
    material = dummy_data_property["constructionmaterial"]
    coordinates = dummy_data[0]["geometry"]["coordinates"][0]
    size = dummy_data_property["geometry_area_m2"]
    osid = dummy_data_property["osid"]
    age_updated_date = dummy_data_property["buildingage_updatedate"]
    property = Property(
        uprn,
        year,
        connectivity,
        material,
        coordinates,
        size,
        osid,
        age_updated_date,
    )
    yield property


def test_property_class_has_correct_attributes_from_dummy_data(dummy_property):

    assert dummy_property.uprn == 100090062842
    assert dummy_property.year == 1959
    assert dummy_property.connectivity == "Single-Connected"
    assert dummy_property.material == "Brick Or Block Or Stone"
    assert dummy_property.coordinates == [
        [0.0452889, 52.4569136],
        [0.0453246, 52.4569215],
        [0.045323, 52.4569242],
        [0.0453908, 52.4569392],
        [0.0454023, 52.4569199],
        [0.0455166, 52.4569451],
        [0.0455493, 52.4568931],
        [0.0453653, 52.4568526],
        [0.0453603, 52.456861],
        [0.0453246, 52.4568531],
        [0.0452889, 52.4569136],
    ]

    assert dummy_property.age_updated_date == "2024-05-20"
    assert dummy_property.size == 111.601
    assert dummy_property.osid == "02ae4ae4-6119-4d72-aef9-e56013d25e0d"
