import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from src.property import Property
from src.utils import SortProperties

properties = [Property(1, 2000, "End-Connected", "", [], 0, "", ""), Property(1, "None", "End-Connected", "", [], 0, "", "")]

 
def test_get_hardest_to_heat_properties_with_empty_array():
    
    result = SortProperties.get_hardest_to_heat_properties([])
    
    assert result == []

def test_get_hardest_to_heat_properties_with_one_property():
    
    property = Property(1, 2000, "End-Connected", "", [], 0, "", "")
    property.calculate_score()
    result = SortProperties.get_hardest_to_heat_properties([property])
    
    
    assert result[0].score == 1
    assert len(result) == 1
    

def test_get_hardest_to_heat_properties_with_multiple_properties():
    
    properties = [Property(1, 2000, "End-Connected", "", [], 0, "", ""), Property(1, "None", "End-Connected", "", [], 0, "", "")]
    
    for property in properties:
        property.calculate_score()
       

    result = SortProperties.get_hardest_to_heat_properties(properties)

    assert result[0].score >= result[1].score  
    assert len(result) == 2