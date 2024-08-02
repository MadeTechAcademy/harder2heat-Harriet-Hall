from src.property import Property
import pytest
import json

with open("./properties.json", "r") as data:
    dummy_data = json.load(data)
    dummy_data_properties = dummy_data[0]["properties"]
 
  
@pytest.fixture
def dummy_property():
    property = Property(dummy_data_properties["uprnreference"][0]["uprn"])    
    yield property


def test_property_class_has_correct_attributes_from_dummy_data(dummy_property):
    dummy_property.connectivity = dummy_data_properties["connectivity"]
    dummy_property.year = dummy_data_properties["buildingage_year"]
    dummy_property.material = dummy_data_properties["constructionmaterial"]
    coordinates_list = dummy_data[0]["geometry"]["coordinates"][0]
    dummy_property.coordinates = coordinates_list
    dummy_property.long = coordinates_list[0][0]
    dummy_property.lat = coordinates_list[0][1]
    dummy_property.size = dummy_data_properties["geometry_area_m2"]
    dummy_property.osid = dummy_data_properties["osid"]
    dummy_property.age_updated_date = dummy_data_properties["buildingage_updatedate"]
    
    
    assert dummy_property.uprn == 100090062842
    assert dummy_property.year == "None"
    assert dummy_property.connectivity == "Semi-Connected"
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
 

    assert dummy_property.age_updated_date == "2024-05-20"
    assert dummy_property.size == 111.601
    assert dummy_property.osid == "02ae4ae4-6119-4d72-aef9-e56013d25e0d"
    
 
def test_handle_year_string_with_buildingage_year_as_None(dummy_property):
    dummy_property.year = dummy_data_properties["buildingage_year"]
    dummy_property.handle_year_string()
    assert dummy_property.year == 1959

def test_handle_year_string_with_buildingage_year(dummy_property):
    dummy_property.year = 1999
    dummy_property.handle_year_string()
    assert dummy_property.year == 1999
 
    
def test_handle_year_string_with_buildingage_year_is_period(dummy_property):
    dummy_property.year = dummy_data_properties["buildingage_period"]
    dummy_property.handle_year_string()
    assert dummy_property.year == 1989

     
def test_handle_connectivity_with_semi_connected(dummy_property):
    dummy_property.connectivity = dummy_data_properties["connectivity"]
    dummy_property.handle_connectivity()
    assert dummy_property.connectivity == "Dual-Connected"
    