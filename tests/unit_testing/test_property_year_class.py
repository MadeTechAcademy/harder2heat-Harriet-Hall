from src.property import MINIMUM_FAILING_YEAR
from src.utils import HandleYear


def test_handle_year_string_with_year_as_None():

    property_year = HandleYear.handle_year_string("None")
    assert property_year == MINIMUM_FAILING_YEAR


def test_handle_year_string_with_year_as_empty_string():

    property_year = HandleYear.handle_year_string("")
    assert property_year == 1959


def test_handle_year_string_with_year_as_integer():

    property_year = HandleYear.handle_year_string(1999)
    assert property_year == 1999


def test_handle_year_string_with_buildingage_period():

    property_year = HandleYear.handle_year_string("1980-1989")
    assert property_year == 1989
