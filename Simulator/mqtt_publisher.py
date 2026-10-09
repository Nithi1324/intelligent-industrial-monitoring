
import json
import time

import paho.mqtt.client as mqtt

from simulator import simulator as machine_simulator

BROKER = "test.mosquitto.org"
PORT = 1883
TOPIC_PREFIX = "intelligent-industrial-monitoring/demo/machines"


def on_connect(client, userdata, flags, reason_code, properties):
    if reason_code == 0:
        print("Connected to MQTT broker successfully.")
    else:
        print(f"MQTT connection failed: {reason_code}")


client = mqtt.Client(
    mqtt.CallbackAPIVersion.VERSION2,
    client_id="industrial-demo-publisher"
)
client.on_connect = on_connect

try:
    print(f"Connecting to {BROKER}:{PORT}...")
    client.connect(BROKER, PORT, keepalive=60)
    client.loop_start()

    time.sleep(2)

    while True:
        for machine in machine_simulator.machines:
            reading = machine_simulator.generate_reading(
                machine["id"], machine["mode"]
            )

            topic = f"{TOPIC_PREFIX}/{machine['id']}"
            payload = json.dumps(reading)

            info = client.publish(topic, payload, qos=1)
            info.wait_for_publish()

            if info.rc == mqtt.MQTT_ERR_SUCCESS:
                print(f"Published to {topic}: {payload}")
            else:
                print(f"Publish failed for {machine['id']}")

        print("-" * 60)
        time.sleep(2)

except KeyboardInterrupt:
    print("\nMQTT publisher stopped.")

except Exception as error:
    print(f"MQTT error: {error}")

finally:
    client.loop_stop()
    client.disconnect()