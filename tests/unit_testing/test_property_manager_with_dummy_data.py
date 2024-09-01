import json
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from src.property import Property
from src.property_manager import PropertyManager

with open("./properties.json", "r") as data:
    dummy_data = json.load(data)

property_manager = PropertyManager(dummy_data)

def test_property_manager_has_correct_attributes():
    assert len(property_manager.list_of_properties) == 4
    assert isinstance(property_manager.list_of_properties[0], Property)
    

def test_get_hardest_to_heat_properties_updates_property_score():
    for property in property_manager.list_of_properties:
        assert property.score == 0

    property_manager.get_hardest_to_heat_properties()
    scores = []
    for property in property_manager.list_of_properties:
        scores.append(property.score)
    assert scores == [2, 0, 0, 0]
