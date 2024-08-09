import pytest 
from src.council import Council
from src.french_property import FrenchProperty

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

@pytest.fixture
def french_council():
    french_council = Council("council_1", "France")
    yield french_council 


def test_generate_property_class_list_when_country_is_France(french_council):
    french_council.generate_property_class_list(data)
    assert isinstance(french_council.list_of_properties[0], FrenchProperty)
    french_property = french_council.list_of_properties[0]
    
    assert french_property.uprn == 1
    assert french_property.year == 1988
    assert french_property.connectivity == "Semi-Connected"
    assert french_property.material == "Brick Or Block Or Stone"
    assert french_property.coordinates == [
        [0.0452889, 52.4569136],
        [0.0453246, 52.4569215],
    ]
    assert french_property.age_updated_date == "2024-05-20"
    assert french_property.size == 11
    assert french_property.osid == "123"
    assert french_property.floors == 2
    assert french_property.distance_to_transport == 10

