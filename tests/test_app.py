import pytest
from app import app

def test_index():
    """
    Test if the Flask app route returns a valid response.
    """
    tester = app.test_client()
    response = tester.get('/')
    assert response.status_code == 200
    assert b"Plant Monitoring Dashboard" in response.data
