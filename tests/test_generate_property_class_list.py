from src.utils import generate_property_class_list
from src.property import Property
from src.utils import generate_property_class_list
import json

with open("./properties.json", "r") as data:
    dummy_data = json.load(data)

    properties = generate_property_class_list(dummy_data)


def test_generate_property_class_list_returns_list_of_properties():

    assert type(properties) is list
    assert type(properties[0]) is Property


def test_generate_property_class_list_creates_property_class_with_correct_attributes():
    property = properties[0]

    assert property.uprn == 100090062842
    assert property.year == "1980-1989"
    assert property.connectivity == "Semi-Connected"
    assert property.material == "Brick Or Block Or Stone"
    assert property.coordinates == [
        [0.0452889, 52.4569136],
        [0.0453246, 52.4569215],
        [0.045323, 52.4569242],
        [0.0453908, 52.4569392],
        [0.0454023, 52.4569199],
        [0.0455166, 52.4569451],
        [0.0455493, 52.4568931],
        [0.0453653, 52.4568526],
        [0.0453603, 52.456861],
        [0.0453246, 52.4568531],
        [0.0452889, 52.4569136],
    ]
    assert property.age_updated_date == "2024-05-20"
    assert property.size == 111.601
    assert property.osid == "02ae4ae4-6119-4d72-aef9-e56013d25e0d"
