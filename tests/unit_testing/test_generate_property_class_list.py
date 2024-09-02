import sys
import os

from src.generate_properties import GenerateProperties

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from src.property import Property


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

 {
        "geometry": {
            "coordinates": [
                [
                    [0.0452321, 21.4569136],
                    [0.0453123, 22.4569215],
                ]
            ]
        },
        "properties": {
            "osid": "456",
            "connectivity": "Semi-Connected",
            "uprnreference": [
                {
                    "uprn": 5,
                }
            ],
            "buildingage_year": "None",
            "geometry_area_m2": 15,
            "buildingage_period": "1980-1989",
            "constructionmaterial": "Brick Or Block Or Stone",
            "buildingage_updatedate": "2023-05-20",
        },
    },
)

properites = GenerateProperties.generate_property_class_list(data)

def test_generate_property_class_list_creates_property_instance():
    property = properites[0]
    assert isinstance(properites[0], Property)
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


def test_generate_property_class_list_creates_multiple_property_class_instances():

    assert len(properites) == 2
