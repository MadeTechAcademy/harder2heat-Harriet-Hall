import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from src.property import Property

property = Property(1, 0, "End-Connected", "", [], 0, "", "")


def test_property_has_correct_attributes():

    assert property.uprn == 1
    assert property.get_year() == 0
    assert property.get_connectivity() == "Dual-Connected"
    assert property.material == ""
    assert property.score == 0


def test_property_has_extra_attributes():

    assert property.coordinates == []
    assert property.size == 0
    assert property.osid == ""
    assert property.age_updated_date == ""


def test_property_has_correct_year_when_given_year_as_None():
    property = Property(1, "None", "End-Connected", "", [], 0, "", "")
    assert property.get_year() == 1959


def test_property_has_correct_year_when_given_year_as_empty_string():
    property = Property(1, "", "End-Connected", "", [], 0, "", "")
    assert property.get_year() == 1959


def test_property_has_correct_year_when_given_year_as_integer():
    property = Property(1, 1900, "End-Connected", "", [], 0, "", "")
    assert property.get_year() == 1900


def test_property_has_correct_year_when_given_year_as_period():
    property = Property(1, "1980-1989", "End-Connected", "", [], 0, "", "")
    assert property.get_year() == 1989


def test_property_has_correct_connectivity_when_given_connectivity_as_empty_string():
    property = Property(1, "", "", "", [], 0, "", "")
    assert property.get_connectivity() == ""


def test_property_has_correct_connectivity_when_given_connectivity_as_standalone():
    property = Property(1, "", "Standalone", "", [], 0, "", "")
    assert property.get_connectivity() == "Free-Standing"


def test_property_has_correct_connectivity_when_given_connectivity_as_semi_connected():
    property = Property(1, "", "Semi-Connected", "", [], 0, "", "")
    assert property.get_connectivity() == "Single-Connected"


def test_property_has_correct_connectivity_when_given_connectivity_as_end_connected():
    property = Property(1, "", "End-Connected", "", [], 0, "", "")
    assert property.get_connectivity() == "Dual-Connected"


def test_calculate_score_with_hard_to_heat_attributes():
    property = Property(1, "", "Standalone", "", [], 0, "", "")
    property.calculate_score()
    assert property.score == 3


def test_calculate_score_with_non_hard_to_heat_attributes():
    property = Property(1, 2000, "Semi-Connected", "Concrete", [], 0, "", "")
    property.calculate_score()
    assert property.score == 0

    property = Property(
        1, 1960, "End-Connected", "Brick Or Block Or Stone", [], 0, "", ""
    )
    property.calculate_score()
    assert property.score == 0


def test_calculate_score_with_combination_of_attributes():
    property = Property(1, 2009, "Standalone", "", [], 0, "", "")
    property.calculate_score()
    assert property.score == 2
