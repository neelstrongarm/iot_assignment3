from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import random
import json
import time

client_id = "iotassignment3"
endpoint = "a28bcutatufmo5-ats.iot.us-east-1.amazonaws.com"
root_ca = "AmazonRootCA1.pem"
private_key = "cd1f0bc0c9744eacea28895e1fa2392df9b1a630d1e15e207771001c535560b9-private.pem.key"
certificate = "cd1f0bc0c9744eacea28895e1fa2392df9b1a630d1e15e207771001c535560b9-certificate.pem.crt"

mqtt_client = AWSIoTMQTTClient(client_id)
mqtt_client.configureEndpoint(endpoint, 8883)
mqtt_client.configureCredentials(root_ca, private_key, certificate)
mqtt_client.configureOfflinePublishQueueing(-1)
mqtt_client.configureDrainingFrequency(2)

try:
    mqtt_client.connect()
except Exception as e:
    print(f"Connection failed: {e}")
    exit(1)

def generate_data():
    return {
        "temperature": round(random.uniform(-50, 50), 2),
        "humidity": round(random.uniform(0, 100), 2),
        "co2": round(random.uniform(300, 2000), 2)
    }

while True:
    payload = json.dumps(generate_data())
    mqtt_client.publish("iot/sensor/data", payload, 1)
    print(f"Published: {payload}")
    time.sleep(15)