from src.utils import HandleConnectivity

def test_handle_connectivity_with_empty_string():

    connectivity = HandleConnectivity.handle_connectivity("")
    assert connectivity == ""


def test_handle_connectivity_with_standalone():

    connectivity = HandleConnectivity.handle_connectivity("Standalone")
    assert connectivity == "Free-Standing"


def test_handle_connectivity_with_semi_connected():

    connectivity = HandleConnectivity.handle_connectivity("Semi-Connected")
    assert connectivity == "Single-Connected"


def test_handle_connectivity_with_end_connected():

    connectivity = HandleConnectivity.handle_connectivity("End-Connected")
    assert connectivity == "Dual-Connected"
    
