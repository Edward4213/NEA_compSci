
portfolio = {"bitcoin": 0.05, "ethereum": 1.2, "solana": 10}
def portfolio_values(portfolio):
    pass


def portfolio_weights(portfolio):
    total = total_value(portfolio)
    weights = {}

    for coin in portfolio:
        coin_weight = (portfolio[coin])/(total)
        weights[coin] = coin_weight
    return weights

def total_value(portfolio):
    return sum(portfolio.values())