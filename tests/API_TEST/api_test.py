from unittest.mock import patch
from src.API.api import getWeather

fake_data = {
  'main':{
    'temp': 298.67
  }
}

@patch('requests.get')
def test_getWeather(mock_get):
    """
    Here we are testing reqeusts.get() function to mock API call
    """
    mock_get.return_value.status_code=200
    mock_get.return_value.json.return_value=fake_data

    expected_return=round((298.67-273.15) * 9/5 + 32, 2)
    expected_return=f"Temperature: {expected_return}F\n"
    assert getWeather("38.89","-77.01","alerts")==expected_return
