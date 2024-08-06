from src.french_property import FrenchProperty
from src.property import Property

def test_french_propery_inherits_from_property_class():
    french_property = FrenchProperty(1, 0, "", "", [], 0, "", "", 5, 19)
    assert isinstance(french_property, Property)