from models import call_price, put_price
from portfolio import portfolio, total_value, portfolio_weights

S = 90000
K = 82000
T = 30 / 365
r = 0.04
sigma = 0.50

print(f"The call price is {call_price(S, K, T, r, sigma)}")
print(f"The put price is {put_price(S, K, T, r, sigma)}")
print("Total:", total_value(portfolio))
print("Weights:", portfolio_weights(portfolio))
