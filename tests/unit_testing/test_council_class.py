import pytest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from src.council import Council
from src.property import Property



@pytest.fixture
def uk_council():
    uk_council = Council("council_1", "UK")
    yield uk_council


data = (
    {
        "geometry": {
            "coordinates": [
                [
                    [0.0452889, 52.4569136],
                    [0.0453246, 52.4569215],
                ]
            ]
        },
        "properties": {
            "osid": "123",
            "connectivity": "Semi-Connected",
            "uprnreference": [
                {
                    "uprn": 1,
                }
            ],
            "buildingage_year": 1988,
            "geometry_area_m2": 11,
            "buildingage_period": "1980-1989",
            "constructionmaterial": "Brick Or Block Or Stone",
            "buildingage_updatedate": "2024-05-20",
        },
    },
)


def test_council_class_has_name_attribute(uk_council):
    assert uk_council.name == "council_1"
    assert uk_council.country == "UK"


def test_council_class_has_list_of_properties(uk_council):
    assert type(uk_council.list_of_properties) is list


def test_generate_property_class_list_updates_list_of_properties(uk_council):
    uk_council.generate_property_class_list(data)
    property = uk_council.list_of_properties[0]
    assert isinstance(property, Property)

    assert property.uprn == 1
    assert property.year == 1988
    assert property.connectivity == "Single-Connected"
    assert property.material == "Brick Or Block Or Stone"
    assert property.coordinates == [
        [0.0452889, 52.4569136],
        [0.0453246, 52.4569215],
    ]
    assert property.age_updated_date == "2024-05-20"
    assert property.size == 11
    assert property.osid == "123"



def test_get_hardest_to_heat_properties_updates_property_score(uk_council):

    property_1 = Property(1, 2000, "Semi-Connected", "Concrete", [], 0, "", "")
    property_2 = Property(1, 1900, "Standalone", "", [], 0, "", "")

    uk_council.list_of_properties = [property_1, property_2]
    uk_council.get_hardest_to_heat_properties()
    
    assert property_1.score == 0
    assert property_2.score == 3


def test_get_hardest_to_heat_properties_sorts_list_of_properties_descenting(uk_council):
  
    property_1 = Property(1, 2000, "Semi-Connected", "", [], 0, "", "")
    property_2 = Property(1, 1900, "Standalone", "", [], 0, "", "")

    uk_council.list_of_properties = [property_1, property_2]
    uk_council.get_hardest_to_heat_properties()

    assert uk_council.list_of_properties[0] == property_2
    assert uk_council.list_of_properties[1] == property_1
    