from src.property import Property
import json


def test_property_class_has_correct_attributes():
    property = Property(1)

    assert property.uprn == 1
    assert property.epc_rating == ""
    assert property.epc_score == ""
    assert property.address == ""
    assert property.year == 0
    assert property.connectivity == ""
    assert property.material == ""
    assert property.score == 0
    assert property.void == False
    assert property.long == 0
    assert property.lat == 0


def test_property_class_has_extra_attributes():
    property = Property(1)

    assert property.coordinates == []
    assert property.size == ""
    assert property.osid == ""
    assert property.age_updated_date == ""


with open("./properties.json", "r") as data:
    dummy_data = json.load(data)
    dummy_data_properties = dummy_data[0]["properties"]
    dummy_property = Property(dummy_data_properties["uprnreference"][0]["uprn"])


def test_property_class_has_correct_attributes_from_dummy_data():
    dummy_property.connectivity = dummy_data_properties["description"]
    dummy_property.year = dummy_data_properties["buildingage_period"]
    dummy_property.material = dummy_data_properties["constructionmaterial"]
    coordinates_list = dummy_data[0]["geometry"]["coordinates"][0]
    dummy_property.coordinates = coordinates_list
    dummy_property.long = coordinates_list[0][0]
    dummy_property.lat = coordinates_list[0][1]

    assert dummy_property.uprn == 100090062842
    assert dummy_property.year == "1980-1989"
    assert dummy_property.connectivity == "Semi-Detached House"
    assert dummy_property.material == "Brick Or Block Or Stone"
    assert dummy_property.coordinates == [
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
 
    assert dummy_property.long == 0.0452889
    assert dummy_property.lat == 52.4569136

