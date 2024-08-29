import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from src.property import Property

property = Property(1, 0, "End-Connected", "", [], 0, "", "")


def test_property_has_correct_attributes():

    assert property.uprn == 1
    assert property.year == 0
    assert property.connectivity == "Dual-Connected"
    assert property.material == ""
    assert property.score == 0


def test_property_has_extra_attributes():

    assert property.coordinates == []
    assert property.size == 0
    assert property.osid == ""
    assert property.age_updated_date == ""


def test_calculate_score_with_hard_to_heat_attributes():
    property.connectivity = "Free-Standing"
    property.material = "not warm material"
    property.year = 1959
    property.calculate_score()
    assert property.score == 3


def test_calculate_score_with_non_hard_to_heat_attributes():

    property.connectivity = "Dual-Connected"
    property.material = "Concrete"
    property.year = 2000
    property.calculate_score()
    assert property.score == 0


def test_calculate_score_with_combination_of_attributes():

    property.connectivity = "Free-Standing"
    property.material = ""
    property.year =  2009
    property.calculate_score()
    assert property.score == 2
