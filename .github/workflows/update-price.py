import os
import json
from datetime import datetime

print("Start update stock price")

data = {
    "update_time": datetime.utcnow().isoformat(),
    "prices": {
        "AAPL": 0,
        "INTC": 0,
        "TSLA": 0,
        "SKHY": 0,
        "DRAM": 0,
        "NOK": 0,
        "SGOV": 0
    }
}

os.makedirs("data", exist_ok=True)

with open("data/prices.json", "w") as f:
    json.dump(data, f, indent=4)

print("Update finished")
