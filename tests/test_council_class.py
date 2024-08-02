from src.council import Council

council = Council("council_1")
def test_council_class_has_name_attribute():
    assert council.name == "council_1"

def test_council_class_has_list_of_properties():
    assert type(council.list_of_properties) is list
