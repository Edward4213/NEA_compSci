from coingecko import get_prices
from portfolio import portfolio

crypto_ids = list(portfolio.keys())

prices = get_prices(crypto_ids)

print("Prices:", prices)