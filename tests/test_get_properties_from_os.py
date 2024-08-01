from src.utils import get_properties_from_os
from src.property import Property
from src.utils import get_properties_from_os
import json

with open("../properties.json", "r") as data:
    dummy_data = json.load(data)

    properties = get_properties_from_os(dummy_data)


def test_get_properties_from_os_returns_list_of_properties():

    assert type(properties) is list
    assert type(properties[0]) is Property
