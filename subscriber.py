from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import json
from datetime import datetime

client_id = "iotassignment3_subscriber"
endpoint = "a28bcutatufmo5-ats.iot.us-east-1.amazonaws.com"
root_ca = "AmazonRootCA1.pem"
private_key = "cd1f0bc0c9744eacea28895e1fa2392df9b1a630d1e15e207771001c535560b9-private.pem.key"
certificate = "cd1f0bc0c9744eacea28895e1fa2392df9b1a630d1e15e207771001c535560b9-certificate.pem.crt"

topic = "iot/sensor/data"
log_file = "data_log.json"

def on_message(client, userdata, message):
    try:
        data = json.loads(message.payload.decode())
        data["timestamp"] = datetime.utcnow().isoformat()

        with open(log_file, "a") as f:
            f.write(json.dumps(data) + "\n")

        print(f"Logged: {data}")
    except Exception as e:
        print(f"Failed to log message: {e}")

mqtt_client = AWSIoTMQTTClient(client_id)
mqtt_client.configureEndpoint(endpoint, 8883)
mqtt_client.configureCredentials(root_ca, private_key, certificate)

mqtt_client.connect()
mqtt_client.subscribe(topic, 1, on_message)

print(f"Subscribed to {topic}. Logging incoming data...")
while True:
    pass