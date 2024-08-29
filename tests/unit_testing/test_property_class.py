import sys
import os

from src.utils import handle_connectivity, handle_year_string

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from src.property import Property

property = Property(1, 0, "", "", [], 0, "", "")


def test_property_has_correct_attributes():

    assert property.uprn == 1
    assert property.year == 0
    assert property.connectivity == ""
    assert property.material == ""
    assert property.score == 0


def test_property_has_extra_attributes():

    assert property.coordinates == []
    assert property.size == 0
    assert property.osid == ""
    assert property.age_updated_date == ""


def test_handle_year_string_with_year_as_None():
    property.year = "None"
    year = handle_year_string(property.year)

    assert year == 1959


def test_handle_year_string_with_year_known():
    property.year = 1999
    year = handle_year_string(property.year)
    assert year == 1999


def test_handle_year_string_with_buildingage_period():
    property.year = "1980-1989"
    year = handle_year_string(property.year)
    assert year == 1989


def test_handle_connectivity_with_standalone():
    property.connectivity = "Standalone"
    connectivity = handle_connectivity(property.connectivity)
    assert connectivity == "Free-Standing"


def test_handle_connectivity_with_semi_connected():
    property.connectivity = "Semi-Connected"
    connectivity = handle_connectivity(property.connectivity)
    assert connectivity == "Single-Connected"


def test_handle_connectivity_with_end_connected():
    property.connectivity = "End-Connected"
    connectivity = handle_connectivity(property.connectivity)
    assert connectivity == "Dual-Connected"


def test_calculate_score_with_hard_to_heat_attributes():
    property.connectivity = "Standalone"
    property.material = "not warm material"
    property.year = "None"
    property.calculate_score()
    assert property.score == 3


def test_calculate_score_with_non_hard_to_heat_attributes():

    property.connectivity = "End-Connected"
    property.material = "Contrete"
    property.year = 2000
    property.calculate_score()
    assert property.score == 0


def test_calculate_score_with_combination_of_attributes():

    property.connectivity = "Standalone"
    property.material = ""
    property.year = "2000-2009"
    property.calculate_score()
    assert property.score == 1
