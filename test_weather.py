# test_weather.py

from dashboard.api_client import get_air_quality

result = get_air_quality("Delhi")

print(result)