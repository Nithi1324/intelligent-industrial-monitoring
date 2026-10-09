
import random
import time
from datetime import datetime


def generate_reading(machine_id, mode):
    temperature = round(random.uniform(40, 50), 2)
    pressure = round(random.uniform(2, 4), 2)
    speed = round(random.uniform(1000, 1500), 2)
    vibration = round(random.uniform(1.0, 2.5), 2)
    current = round(random.uniform(1.5, 2.5), 2)

    if mode == "machine_fault":
        temperature = round(random.uniform(75, 95), 2)
        pressure = round(random.uniform(5, 8), 2)
        speed = round(random.uniform(500, 800), 2)
        vibration = round(random.uniform(5.0, 8.0), 2)
        current = round(random.uniform(3.0, 4.5), 2)

    elif mode == "sensor_fault":
        temperature = 45.0

    return {
        "timestamp": datetime.now().isoformat(timespec="seconds"),
        "machine_id": machine_id,
        "temperature": temperature,
        "pressure": pressure,
        "speed": speed,
        "vibration": vibration,
        "current": current,
        "mode": mode,
    }


machines = [
    {"id": "M001", "mode": "normal"},
    {"id": "M002", "mode": "machine_fault"},
    {"id": "M003", "mode": "sensor_fault"},
]


if __name__ == "__main__":
    try:
        while True:
            for machine in machines:
                reading = generate_reading(
                    machine["id"], machine["mode"]
                )
                print(reading)

            print("-" * 70)
            time.sleep(2)

    except KeyboardInterrupt:
        print("\nSimulation stopped.")