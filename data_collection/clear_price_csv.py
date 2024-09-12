# clear_bitcoin_prices.py

# Define the file path for the CSV file
file_path = 'data/bitcoin_prices.csv'

# Open the file in write mode to clear the content
with open(file_path, 'w') as file:
    # Optionally, write the header back with the new currencies
    file.write('timestamp,btc_usd_price,btc_eur_price,btc_jpy_price,btc_gbp_price,btc_brl_price,btc_vnd_price,'
               'btc_aed_price,btc_rub_price,btc_ngn_price,btc_cny_price,btc_inr_price,btc_krw_price\n')

print(f"Cleared the contents of {file_path}.")