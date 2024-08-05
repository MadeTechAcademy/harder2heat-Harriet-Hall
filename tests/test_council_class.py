from src.council import Council
from src.property import Property


council = Council("council_1")
data = (
    {
        "geometry": {
            "coordinates": [
                [
                    [0.0452889, 52.4569136],
                    [0.0453246, 52.4569215],
                ]
            ]
        },
        "properties": {
            "osid": "123",
            "connectivity": "Semi-Connected",
            "uprnreference": [
                {
                    "uprn": 1,
                }
            ],
            "buildingage_year": 1988,
            "geometry_area_m2": 11,
            "buildingage_period": "1980-1989",
            "constructionmaterial": "Brick Or Block Or Stone",
            "buildingage_updatedate": "2024-05-20",
        },
    },
    
)

def test_council_class_has_name_attribute():
    assert council.name == "council_1"


def test_council_class_has_list_of_properties():
    assert type(council.list_of_properties) is list


def test_generate_property_class_list_updates_list_of_properties():
    council.generate_property_class_list(data)
    assert type(council.list_of_properties[0]) is Property

    property = council.list_of_properties[0]
    assert property.uprn == 1
    assert property.year == 1988
    assert property.connectivity == "Semi-Connected"
    assert property.material == "Brick Or Block Or Stone"
    assert property.coordinates == [
        [0.0452889, 52.4569136],
        [0.0453246, 52.4569215],
    ]
    assert property.age_updated_date == "2024-05-20"
    assert property.size == 11
    assert property.osid == "123"


property_1 = Property(1, 2000, "", "", [], 0, "", "")
property_2 = Property(1, 1900, "", "", [], 0, "", "")

def test_get_hardest_to_heat_properties_updates_property_score():
    council.list_of_properties = [property_1, property_2]
    council.get_hardest_to_heat_properties()

    assert property_1.score == 0
    assert property_2.score == 1


def test_get_hardest_to_heat_properties_sorts_list_of_properties_descenting():
    council.list_of_properties = [property_1, property_2]
    council.get_hardest_to_heat_properties()

    assert council.list_of_properties[0].score == 1
    assert council.list_of_properties[1].score == 0
