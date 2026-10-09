
import json

import paho.mqtt.client as mqtt

BROKER = "test.mosquitto.org"
PORT = 1883
TOPIC = "intelligent-industrial-monitoring/demo/machines/#"


def on_connect(client, userdata, flags, reason_code, properties):
    if reason_code == 0:
        print("Connected to MQTT broker.")
        client.subscribe(TOPIC, qos=1)
        print(f"Listening to topic: {TOPIC}")
    else:
        print(f"Connection failed: {reason_code}")


def on_message(client, userdata, message):
    try:
        reading = json.loads(message.payload.decode("utf-8"))
        print(f"\nTopic: {message.topic}")
        print(f"Machine: {reading['machine_id']}")
        print(f"Temperature: {reading['temperature']}")
        print(f"Pressure: {reading['pressure']}")
        print(f"Speed: {reading['speed']}")
        print(f"Vibration: {reading['vibration']}")
        print(f"Current: {reading['current']}")
        print(f"Mode: {reading['mode']}")
    except (ValueError, KeyError) as error:
        print(f"Invalid message: {error}")


client = mqtt.Client(
    mqtt.CallbackAPIVersion.VERSION2,
    client_id="industrial-demo-subscriber"
)
client.on_connect = on_connect
client.on_message = on_message

try:
    print(f"Connecting to {BROKER}:{PORT}...")
    client.connect(BROKER, PORT, keepalive=60)
    client.loop_forever()

except KeyboardInterrupt:
    print("\nMQTT subscriber stopped.")

except Exception as error:
    print(f"MQTT error: {error}")

finally:
    client.disconnect()