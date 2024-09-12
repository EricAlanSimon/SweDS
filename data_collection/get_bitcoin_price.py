import requests
import pandas as pd
from datetime import datetime

# Define the URL for the CoinGecko API
coingecko_url = "https://api.coingecko.com/api/v3/simple/price"
params = {
    "ids": "bitcoin", 
    "vs_currencies": "usd,eur,jpy,gbp,brl,vnd,aed,rub,ngn,cny,inr,krw"  # Adding all currencies
}

# Send the request to CoinGecko API
response = requests.get(coingecko_url, params=params)

# Check if the response is successful
if response.status_code == 200:
    data = response.json()
    
    # Extract relevant data for each currency
    price_usd = float(data['bitcoin']['usd'])
    price_eur = float(data['bitcoin']['eur'])
    price_jpy = float(data['bitcoin']['jpy'])
    price_gbp = float(data['bitcoin']['gbp'])
    price_brl = float(data['bitcoin']['brl'])  # Brazilian Real
    price_vnd = float(data['bitcoin']['vnd'])  # Vietnamese Dong
    price_aed = float(data['bitcoin']['aed'])  # UAE Dirham
    price_rub = float(data['bitcoin']['rub'])  # Russian Ruble
    price_ngn = float(data['bitcoin']['ngn'])  # Nigerian Naira
    price_cny = float(data['bitcoin']['cny'])  # Chinese Yuan
    price_inr = float(data['bitcoin']['inr'])  # Indian Rupee
    price_krw = float(data['bitcoin']['krw'])  # Korean Won
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Save the data to a CSV file
    df = pd.DataFrame([[timestamp, price_usd, price_eur, price_jpy, price_gbp, price_brl, price_vnd, price_aed, 
                        price_rub, price_ngn, price_cny, price_inr, price_krw]], 
                      columns=['timestamp', 'btc_usd_price', 'btc_eur_price', 'btc_jpy_price', 
                               'btc_gbp_price', 'btc_brl_price', 'btc_vnd_price', 'btc_aed_price',
                               'btc_rub_price', 'btc_ngn_price', 'btc_cny_price', 'btc_inr_price', 
                               'btc_krw_price'])
    
    # Append the data to the CSV file
    df.to_csv('data/bitcoin_prices.csv', mode='a', header=False, index=False)
    
    # Print confirmation
    print(f"Data saved: {timestamp}, BTC Prices: USD: {price_usd}, EUR: {price_eur}, JPY: {price_jpy}, GBP: {price_gbp}, "
          f"BRL: {price_brl}, VND: {price_vnd}, AED: {price_aed}, RUB: {price_rub}, NGN: {price_ngn}, "
          f"CNY: {price_cny}, INR: {price_inr}, KRW: {price_krw}")
else:
    print("Failed to retrieve data")
