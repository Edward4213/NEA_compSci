import requests

def get_prices(crypto_ids):
    url = "https://api.coingecko.com/api/v3/simple/price"
    parameters = {"ids": ",".join(crypto_ids), "vs_currencies": "gbp"}
    try:
        response = requests.get(url, params=parameters,timeout=10.)
        response.raise_for_status()
        return response.json()
    except requests.RequestException:
        print("Unable to retrieve cryptocurrency prices.")
        return {}

cryptos = ["bitcoin", "ethereum", "solana"]

prices = get_prices(cryptos)

print("Bitcoin:", prices["bitcoin"]["gbp"])
print("Ethereum:", prices["ethereum"]["gbp"])
print("Solana:", prices["solana"]["gbp"])