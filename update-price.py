import os
import json
import requests
from datetime import datetime, timezone


API_KEY = os.environ.get("FINNHUB_API_KEY")

if not API_KEY:
    raise Exception("FINNHUB_API_KEY is missing")


SYMBOLS = [
    "AAPL",
    "INTC",
    "TSLA",
    "SKHY",
    "DRAM",
    "NOK",
    "SGOV"
]


def get_price(symbol):
    url = "https://finnhub.io/api/v1/quote"

    params = {
        "symbol": symbol,
        "token": API_KEY
    }

    try:
        response = requests.get(
            url,
            params=params,
            timeout=10
        )

        data = response.json()

        print(symbol, data)

        price = data.get("c")

        if price and price > 0:
            return round(price, 4)

        return None

    except Exception as e:
        print("ERROR:", symbol, e)
        return None



prices = {}

for symbol in SYMBOLS:
    prices[symbol] = get_price(symbol)



result = {
    "update_time": datetime.now(
        timezone.utc
    ).isoformat(),

    "prices": prices
}


os.makedirs(
    "data",
    exist_ok=True
)


with open(
    "data/prices.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        result,
        f,
        indent=4,
        ensure_ascii=False
    )


print("DONE")
