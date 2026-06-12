import time

from python_simulation.simulator import generate_sensor_packet
from python_simulation.aqi_engine import classify_air_quality
from python_simulation.alerts import generate_alert
from python_simulation.logger import save_record

NUM_RECORDS = 100

for _ in range(NUM_RECORDS):

    data = generate_sensor_packet()

    status = classify_air_quality(data["aqi"])

    alert = generate_alert(data["aqi"])

    record = {
        "timestamp": data["timestamp"],
        "aqi": data["aqi"],
        "pm25": data["pm25"],
        "pm10": data["pm10"],
        "temperature": data["temperature"],
        "humidity": data["humidity"],
        "status": status,
        "alert": alert[1]
    }

    print(record)

    save_record(record)

    time.sleep(1)

print("Simulation Complete")