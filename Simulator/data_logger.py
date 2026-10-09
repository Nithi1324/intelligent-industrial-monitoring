
import csv
import os
import time

from simulator.simulator import generate_reading, machines

CSV_FILE = "sensor_data.csv"

FIELDS = [
    "timestamp",
    "machine_id",
    "temperature",
    "pressure",
    "speed",
    "vibration",
    "current",
    "mode",
]

def save_reading(reading):
    file_exists = os.path.exists(CSV_FILE)
    write_header = not file_exists or os.path.getsize(CSV_FILE) == 0

    with open(CSV_FILE, "a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)

        if write_header:
            writer.writeheader()

        writer.writerow(reading)


if __name__ == "__main__":
    print("Sensor data logger started.")
    print(f"Saving readings to {CSV_FILE}")
    print("Press Ctrl+C to stop.")

    try:
        while True:
            for machine in machines:
                reading = generate_reading(
                    machine["id"], machine["mode"]
                )

                save_reading(reading)

                print(
                    f"Saved: {reading['machine_id']} | "
                    f"Temperature: {reading['temperature']} | "
                    f"Mode: {reading['mode']}"
                )

            print("-" * 50)
            time.sleep(2)

    except KeyboardInterrupt:
        print("\nData logger stopped.")