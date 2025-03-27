import json
from datetime import datetime, timedelta

log_file = "data_log.json"

sensor_key = input("Enter sensor type (temperature/humidity/co2): ").strip().lower()
cutoff_time = datetime.utcnow() - timedelta(hours=5)

print(f"\nShowing '{sensor_key}' data from the last 5 hours:\n")

try:
    with open(log_file, "r") as f:
        for line in f:
            try:
                entry = json.loads(line)
                timestamp = datetime.fromisoformat(entry["timestamp"])
                if timestamp >= cutoff_time and sensor_key in entry:
                    print(f"{timestamp}: {entry[sensor_key]}")
            except Exception as e:
                continue
except FileNotFoundError:
    print("Log file not found. Run the subscriber script to collect data first.")