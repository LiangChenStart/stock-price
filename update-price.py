import os
import json
import requests
from datetime import datetime, timezone


# Finnhub API Key
API_KEY = os.environ.get("FINNHUB_API_KEY")

if not API_KEY:
    raise Exception("Missing FINNHUB_API_KEY")


# 你的股票列表
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
    """
    获取 Finnhub 最新价格
    """
    url = "https://finnhub.io/api/v1/quote"

    params = {
        "symbol": symbol,
        "token": API_KEY
    }

    try:
        r = requests.get(url, params=params, timeout=10)
        data = r.json()

        # Finnhub:
        # c = current price
        price = data.get("c")

        if price:
            return round(price, 4)

        return None

    except Exception as e:
        print(symbol, e)
        return None



prices = {}

for symbol in SYMBOLS:
    price = get_price(symbol)

    print(symbol, price)

    prices[symbol] = price


result = {
    "update_time": datetime.now(timezone.utc).isoformat(),
    "prices": prices
}


# 创建目录
os.makedirs("data", exist_ok=True)


# 写入 JSON
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


print("Finished")
