# iot_assignment3
Cloud-based IoT system that collects data from a set of virtual sensors, deployed to collect environmental information using the MQTT protocol.

Methodology
– There are three main code files – publisher.py, subscriber.py and fetch.py

- *publisher.py* – Script simulates sensor data by randomly generating temperature, humidity, and CO2 values. It connects to AWS IoT Core using MQTT protocol. It publishes sensor data to the MQTT topic (iot/sensor/data) every 15 seconds.

- *subscriber.py*  – When new data is published by the publisher.py, this script receives it. The data is logged into a JSON file (data_log.json), along with a timestamp.

- *fetch.py* – The script reads the data_log.json file and extracts sensor data from the last 5 hours. The user enters a specific sensor type (temperature, humidity, or CO2), and retrieves the required 5 hour window of said sensor’s data.



