from src.utils import handle_connectivity

def test_handle_connectivity_with_empty_string():
    connectivity = ""
    property_connectivity = handle_connectivity(connectivity)
    assert property_connectivity == ""


def test_handle_connectivity_with_standalone():
    connectivity = "Standalone"
    property_connectivity = handle_connectivity(connectivity)
    assert property_connectivity == "Free-Standing"


def test_handle_connectivity_with_semi_connected():
    connectivity = "Semi-Connected"
    property_connectivity = handle_connectivity(connectivity)
    assert property_connectivity == "Single-Connected"


def test_handle_connectivity_with_end_connected():
    connectivity = "End-Connected"
    property_connectivity = handle_connectivity(connectivity)
    assert property_connectivity == "Dual-Connected"
    
