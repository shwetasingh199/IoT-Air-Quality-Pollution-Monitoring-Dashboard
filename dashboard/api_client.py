import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")


def get_coordinates(city):

    url = (
        f"https://api.openweathermap.org/geo/1.0/direct"
        f"?q={city}&limit=1&appid={API_KEY}"
    )

    response = requests.get(url)

    if response.status_code != 200:
        return None

    data = response.json()

    if len(data) == 0:
        return None

    return data[0]["lat"], data[0]["lon"]


def get_air_quality(city):

    coords = get_coordinates(city)

    if coords is None:
        return None

    lat, lon = coords

    # Air Pollution API
    air_url = (
        f"https://api.openweathermap.org/data/2.5/air_pollution"
        f"?lat={lat}&lon={lon}&appid={API_KEY}"
    )

    air_response = requests.get(air_url)

    if air_response.status_code != 200:
        return None

    air_data = air_response.json()

    # Weather API
    weather_url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?lat={lat}&lon={lon}"
        f"&appid={API_KEY}"
        f"&units=metric"
    )

    weather_response = requests.get(weather_url)
    print("Weather Status:", weather_response.status_code)
    print("Weather Data:", weather_response.json())
    if weather_response.status_code != 200:
        return None

    weather_data = weather_response.json()

    return {
        "aqi": air_data["list"][0]["main"]["aqi"],
        "pm25": air_data["list"][0]["components"]["pm2_5"],
        "pm10": air_data["list"][0]["components"]["pm10"],
        "co": air_data["list"][0]["components"]["co"],
        "temperature": weather_data.get("main", {}).get("temp", None),
        "humidity": weather_data.get("main", {}).get("humidity", None),
        "city": city
    }