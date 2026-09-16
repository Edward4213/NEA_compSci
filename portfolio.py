portfolio={}

def total_value(portfolio):
    return sum(portfolio.values())

def portfolio_weights(portfolio):
    total = total_value(portfolio)
    weights = {}

    for coin in portfolio:
        coin_weight = (portfolio[coin])/(total)
        weights[coin] = coin_weight
    return weights
