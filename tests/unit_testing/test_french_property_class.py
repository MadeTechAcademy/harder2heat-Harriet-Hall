import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from src.french_property import FrenchProperty
from src.property import Property

french_property = FrenchProperty(1, 0, "", "", [], 0, "", "", 5, 19)


def test_french_propery_inherits_from_property_class():
    assert isinstance(french_property, Property)


def test_french_propery_has_correct_attributes():

    assert french_property.uprn == 1
    assert french_property.year == 0
    assert french_property.connectivity == ""
    assert french_property.material == ""
    assert french_property.coordinates == []
    assert french_property.size == 0
    assert french_property.osid == ""
    assert french_property.age_updated_date == ""
    assert french_property.floors == 5
    assert french_property.distance_to_transport == 19
    assert french_property.score == 0
