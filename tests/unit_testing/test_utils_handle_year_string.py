from src.property import Property
from src.utils import handle_year_string


def test_handle_year_string_with_year_as_None():
    year = "None"
    property_year = handle_year_string(year)
    assert property_year == 1959

def test_handle_year_string_with_year_as_empty_string():
    year = ""
    property_year = handle_year_string(year)
    assert property_year == 1959
    
def test_handle_year_string_with_year_as_integer():
    year = 1999
    property_year = handle_year_string(year)
    assert property_year == 1999


def test_handle_year_string_with_buildingage_period():
    year = "1980-1989"
    property_year = handle_year_string(year)
    assert property_year == 1989

