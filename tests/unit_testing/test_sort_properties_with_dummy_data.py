import json
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from src.generate_properties import GenerateProperties
from src.utils import SortProperties

with open("./properties.json", "r") as data:
    dummy_data = json.load(data)
properties_list = GenerateProperties.generate_property_class_list(dummy_data)


def test_get_hardest_to_heat_properties_with_dummy_data():
    
    unsorted_scores = []
    
    for property in properties_list:
        property.calculate_score()
        unsorted_scores.append(property.score)
    

    properties = SortProperties.get_hardest_to_heat_properties(properties_list)

    sorted_scores = []
    
    for property in properties:
        sorted_scores.append(property.score)
    
    assert unsorted_scores == [0, 0, 2, 0]
    assert sorted_scores == [2, 0, 0, 0]