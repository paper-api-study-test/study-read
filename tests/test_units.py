from weatherkit.units import celsius_to_fahrenheit, fahrenheit_to_celsius


def test_round_trip():
    assert round(fahrenheit_to_celsius(celsius_to_fahrenheit(21.5)), 6) == 21.5


def test_freezing_point():
    assert celsius_to_fahrenheit(0) == 32
