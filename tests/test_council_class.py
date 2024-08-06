from src.council import Council
from src.property import Property
from src.french_property import FrenchProperty
import pytest

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
            "number_of_floors" : 2,
            "distance_to_public_transport_meters" : 10
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
    assert isinstance(uk_council.list_of_properties[0], Property) 

    property = uk_council.list_of_properties[0]
    assert property.uprn == 1
    assert property.year == 1988
    assert property.connectivity == "Semi-Connected"
    assert property.material == "Brick Or Block Or Stone"
    assert property.coordinates == [
        [0.0452889, 52.4569136],
        [0.0453246, 52.4569215],
    ]
    assert property.age_updated_date == "2024-05-20"
    assert property.size == 11
    assert property.osid == "123"


property_1 = Property(1, 2000, "", "", [], 0, "", "")
property_2 = Property(1, 1900, "", "", [], 0, "", "")

def test_get_hardest_to_heat_properties_updates_property_score(uk_council):
    uk_council.list_of_properties = [property_1, property_2]
    uk_council.get_hardest_to_heat_properties()

    assert property_1.score == 0
    assert property_2.score == 1


def test_get_hardest_to_heat_properties_sorts_list_of_properties_descenting(uk_council):
    uk_council.list_of_properties = [property_1, property_2]
    uk_council.get_hardest_to_heat_properties()

    assert uk_council.list_of_properties[0].score == 1
    assert uk_council.list_of_properties[1].score == 0

