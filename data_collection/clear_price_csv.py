# clear_bitcoin_prices.py

# Define the file path for the CSV file
file_path = 'data/bitcoin_prices.csv'

# Open the file in write mode to clear the content
with open(file_path, 'w') as file:
    # Optionally, write the header back if needed
    file.write('timestamp,btc_usd_price,btc_eur_price,btc_jpy_price,btc_gbp_price\n')

print(f"Cleared the contents of {file_path}.")
