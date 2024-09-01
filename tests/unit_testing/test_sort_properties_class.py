import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from src.property import Property
from src.utils import SortProperties


properties = [Property(1, 2000, "End-Connected", "", [], 0, "", ""), Property(1, "None", "End-Connected", "", [], 0, "", "")]

 
def test_get_hardest_to_heat_properties_with_empty_array():
    
    properties = SortProperties.get_hardest_to_heat_properties([])
    
    assert properties == []
