from src.property_year import MINIMUM_FAILING_YEAR
from src.property_year import Year


def test_handle_year_string_with_year_as_None():
    year = Year("None")
    property_year = year.handle_year_string("None")
    assert property_year == MINIMUM_FAILING_YEAR


def test_handle_year_string_with_year_as_empty_string():
    year = Year("")
    property_year = year.handle_year_string("")
    assert property_year == 1959


def test_handle_year_string_with_year_as_integer():
    year = Year(1999)
    property_year = year.handle_year_string(1999)
    assert property_year == 1999


def test_handle_year_string_with_buildingage_period():
    year = Year("1980-1989")
    property_year = year.handle_year_string("1980-1989")
    assert property_year == 1989
