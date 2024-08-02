from src.property import Property
property = Property(1)

def test_property_has_correct_attributes():

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


def test_property_has_extra_attributes():

    assert property.coordinates == []
    assert property.size == 0
    assert property.osid == ""
    assert property.age_updated_date == ""
    
    
def test_handle_year_string_with_year_as_None():
    property.year = "None"
    property.handle_year_string()
    assert property.year == 1959
    
def test_handle_year_string_with_year_known():
    property.year = 1999
    property.handle_year_string()
    assert property.year == 1999
    
def test_handle_year_string_with_buildingage_period():
    property.year = "1980-1989"
    property.handle_year_string()
    assert property.year == 1989
