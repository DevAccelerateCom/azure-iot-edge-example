import json
import random
import time
import os
from azure.iot.device import IoTHubDeviceClient

# Read connection string from environment variable
CONNECTION_STRING = os.getenv("IOT_HUB_CONNECTION_STRING")

if not CONNECTION_STRING:
    raise ValueError("The environment variable IOT_HUB_CONNECTION_STRING is not set!")

# Create manual connection
client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)

def monitor_temperature():
    while True:
        temperature = random.uniform(-10, 10)  # Simulating a random temperature
        threshold = 2  # Alert threshold

        if temperature < -threshold or temperature > threshold:
            message = {
                "temperature": temperature,
                "alert": "⚠️ Temperature out of range!"
            }
            print("⚠️ ALERT:", message)
            client.send_message(json.dumps(message))  # Send to cloud
        else:
            print(f"🌡 Temperature OK: {temperature:.2f}°C")

        time.sleep(5)

if __name__ == "__main__":
    try:
        client.connect()
        print("✅ Connection successful!")
    except Exception as e:
        print(f"❌ Connection error: {e}")
    monitor_temperature()
