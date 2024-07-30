from src.property import Property

def test_property_class_has_correct_attributes():
    property = Property(1)
  
    assert property.uprn == 1
    assert property.epc_rating ==  ''
    assert property.epc_score ==  ''
    assert property.address ==  ''
    assert property.age ==  0
    assert property.connectivity ==  ''
    assert property.material ==  ''
    assert property.score ==  0
    assert property.void ==  False
    assert property.long ==  0
    assert property.lat ==  0
    