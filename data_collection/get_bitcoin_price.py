import requests
import pandas as pd
from datetime import datetime

# Define the URL for the CoinGecko API
coingecko_url = "https://api.coingecko.com/api/v3/simple/price"
params = {
    "ids": "bitcoin", 
    "vs_currencies": "usd"
}

# Send a request to the CoinGecko API
response = requests.get(coingecko_url, params=params)

# Check if the response is successful
if response.status_code == 200:
    data = response.json()

    # Extract relevant data (price and time)
    price = float(data['bitcoin']['usd'])
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Save the data to a CSV file
    df = pd.DataFrame([[timestamp, price]], columns=['timestamp', 'btc_usd_price'])
    df.to_csv('data/bitcoin_prices.csv', mode='a', header=False, index=False)
    
    print(f"Data saved: {timestamp}, BTC/USD Price: {price}")
else:
    print("Failed to retrieve data")
