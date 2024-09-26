import requests
import pandas as pd
from datetime import datetime

# Define the base URL for Binance API
binance_url = "https://api.binance.com/api/v3/klines"

# Function to fetch historical Bitcoin prices from Binance
def fetch_historical_prices(symbol, interval="1d", limit=30):
    params = {
        "symbol": symbol,
        "interval": interval,  # 1d = daily interval
        "limit": limit  # Number of data points (days)
    }

    # Send the request to Binance API
    response = requests.get(binance_url, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        return response.json()  # Return the OHLC data
    else:
        print(f"Failed to retrieve data for {symbol}, Status Code: {response.status_code}")
        return []

# Fetch historical data for Bitcoin (BTCUSDT) - last 365 days
historical_data = fetch_historical_prices("BTCUSDT", limit=365)

# Initialize an empty list to store the data
all_data = []

# Process and append the data
for price_data in historical_data:
    timestamp = datetime.utcfromtimestamp(price_data[0] / 1000).strftime('%Y-%m-%d')
    price = price_data[4]  # Close price is at index 4 in the Binance API response
    all_data.append([timestamp, 'usd', price])

# Convert the data into a DataFrame
df = pd.DataFrame(all_data, columns=['timestamp', 'currency', 'btc_price'])

# Save the data to a CSV file
df.to_csv('data/bitcoin_historical_prices_binance.csv', index=False)

# Print confirmation
print("Historical data saved successfully!")
