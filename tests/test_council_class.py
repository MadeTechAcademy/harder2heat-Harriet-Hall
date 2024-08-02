from src.council import Council

def test_council_class_has_name_attribute():
    council = Council("council_1")
    assert council.name == "council_1"