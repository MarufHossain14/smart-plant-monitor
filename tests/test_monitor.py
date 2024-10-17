import pytest
from monitor import read_sensors

def test_read_sensors():
    """
    Test if the read_sensors function returns valid data types.
    """
    humidity, temperature, soil_moisture, light = read_sensors()
    assert isinstance(humidity, (float, type(None)))
    assert isinstance(temperature, (float, type(None)))
    assert isinstance(soil_moisture, int)
    assert isinstance(light, int)
