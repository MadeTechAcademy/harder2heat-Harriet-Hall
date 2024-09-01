import json
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from src.property import Property
from src.property_manager import PropertyManager



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
            "constructionmaterial": "",
            "buildingage_updatedate": "2023-05-20",
        },
    },
)

property_manager = PropertyManager(data)


def test_property_manager_has_correct_attributes():
    assert len(property_manager.list_of_properties) == 2
    assert isinstance(property_manager.list_of_properties[0], Property)
    
