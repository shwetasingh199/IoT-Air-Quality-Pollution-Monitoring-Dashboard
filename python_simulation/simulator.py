import random
from datetime import datetime


def generate_sensor_packet():
    return {
        "timestamp": datetime.now(),
        "aqi": random.randint(20, 450),
        "pm25": round(random.uniform(5, 300), 2),
        "pm10": round(random.uniform(10, 400), 2),
        "temperature": round(random.uniform(18, 42), 2),
        "humidity": round(random.uniform(30, 90), 2)
    }