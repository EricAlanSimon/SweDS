# data_collection/get_bitcoin_price.py

import requests
import pandas as pd
from datetime import datetime

# Define the URL for the Binance API
binance_url = "https://api.binance.com/api/v3/ticker/price"
symbol = "BTCUSDT"  # This represents the BTC to USD trading pair

# Send a request to the API
response = requests.get(binance_url, params={"symbol": symbol})

# Check if the response is successful
if response.status_code == 200:
    data = response.json()

    # Extract relevant data (price and time)
    price = float(data['price'])
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Save the data to a CSV file
    df = pd.DataFrame([[timestamp, price]], columns=['timestamp', 'btc_usd_price'])
    df.to_csv('data/bitcoin_prices.csv', mode='a', header=False, index=False)
    
    print(f"Data saved: {timestamp}, BTC/USD Price: {price}")
else:
    print("Failed to retrieve data")
