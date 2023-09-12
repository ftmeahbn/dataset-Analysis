import requests
import json

url = "https://rest.coinapi.io/v1/exchangerate/BTC/USD"
api_key = "F5869FD6-694F-4486-98A1-D7829EB3DC0F"

date = input("Enter Date (YYYY-MM-DD): ")
formatted_date = date.replace("/", "-")

headers = {"X-CoinAPI-Key": api_key}

response = requests.get(url, headers=headers, params={"time": formatted_date})


if response.status_code == 200:
    data = response.json()
    if "rate" in data:
        btc_price = data["rate"]
        print(f"BTC Price on {date}: {btc_price} USD")
    else:
        print("BTC price data not available for the specified date.")
else:
    print("Error in retrieving BTC price data.")
