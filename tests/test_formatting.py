from weatherkit.formatting import format_current


def test_metric():
    data = {"city": "Madrid", "temp_c": 20.04, "temp_f": 68.1, "condition": "Sunny"}
    assert format_current(data) == "Madrid: 20.0 C, Sunny"
