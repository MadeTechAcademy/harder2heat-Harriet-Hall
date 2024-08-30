from src.property_connectivity import Connectivity


def test_handle_connectivity_with_empty_string():
    connectivity = Connectivity("")
    property_connectivity = connectivity.handle_connectivity("")
    assert property_connectivity == ""


def test_handle_connectivity_with_standalone():
    connectivity = Connectivity("Standalone")
    property_connectivity = connectivity.handle_connectivity("Standalone")
    assert property_connectivity == "Free-Standing"


def test_handle_connectivity_with_semi_connected():
    connectivity = Connectivity("Semi-Connected")
    property_connectivity = connectivity.handle_connectivity("Semi-Connected")
    assert property_connectivity == "Single-Connected"


def test_handle_connectivity_with_end_connected():
    connectivity = Connectivity("End-Connected")
    property_connectivity = connectivity.handle_connectivity("End-Connected")
    assert property_connectivity == "Dual-Connected"


def test_get_connectivity():
    connectivity = Connectivity("End-Connected")
    property_connectivity = connectivity.get_connectivity()
    assert property_connectivity == "Dual-Connected"