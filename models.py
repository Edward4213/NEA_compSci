import math
from scipy.stats import norm

def d1(S,K,T,r,sigma):
    d1 = (math.log(S/K) + (r + ((sigma**2)/2))*T)/(sigma*math.sqrt(T))
    return d1

def d2(S,K,T,r,sigma):
    d2 = d1(S,K,T,r,sigma) - sigma*math.sqrt(T)
    return d2

def call_price(S,K,T,r,sigma):

    d1_value = d1(S,K,T,r,sigma)
    d2_value = d2(S,K,T,r,sigma)

    call_price_value = S*(norm.cdf(d1_value)) - K*math.exp(-r*T)*norm.cdf(d2_value)
    return call_price_value

def put_price(S,K,T,r,sigma):

    d1_value = d1(S,K,T,r,sigma)
    d2_value = d2(S,K,T,r,sigma)

    put_price_value = K*math.exp(-r*T)*norm.cdf(d2_value) - S*(norm.cdf(d1_value))
    return put_price_value
