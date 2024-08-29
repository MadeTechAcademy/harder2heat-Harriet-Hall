import pytest
import json
import sys
import os

from src.utils import handle_connectivity, handle_year_string

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
    assert dummy_property.year == "None"
    assert dummy_property.connectivity == "Semi-Connected"
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


def test_handle_year_string_with_buildingage_year_as_None(dummy_property):
    dummy_property.year = dummy_data_property["buildingage_year"]
    assert dummy_property.year == "None"
    year = handle_year_string(dummy_property.year)
    assert year == 1959


def test_handle_year_string_with_buildingage_year_is_period(dummy_property):
    dummy_property.year = dummy_data_property["buildingage_period"]
    assert dummy_property.year == "1980-1989"
    year = handle_year_string(dummy_property.year)
    assert year == 1989


def test_handle_connectivity_with_semi_connected(dummy_property):
    dummy_property.connectivity = dummy_data_property["connectivity"]
    assert dummy_property.connectivity == "Semi-Connected"
    connectivity = handle_connectivity(dummy_property.connectivity)
    assert connectivity == "Single-Connected"


dummy_end_connected = dummy_data[1]["properties"]

@pytest.fixture
def dummy_property_1():
    uprn = dummy_end_connected["uprnreference"][0]["uprn"]
    connectivity = dummy_data[1]["properties"]["connectivity"]
    property = Property(uprn, 0, connectivity, "", [], "", "", "")
    yield property


def test_handle_connectivity_with_end_connected(dummy_property_1):

    assert dummy_property_1.connectivity == "End-Connected"
    connectivity = handle_connectivity(dummy_property_1.connectivity)
    assert connectivity == "Dual-Connected"


dummy_standalone = dummy_data[2]["properties"]


@pytest.fixture
def dummy_property_2():
    uprn = dummy_standalone["uprnreference"][0]["uprn"]
    connectivity = dummy_standalone["connectivity"]
    property = Property(uprn, 0, connectivity, "", [], "", "", "")
    yield property


def test_handle_connectivity_with_standalone(dummy_property_2):
    assert dummy_property_2.connectivity == "Standalone"
    connectivity = handle_connectivity(dummy_property_2.connectivity)
    assert connectivity == "Free-Standing"
