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

def call_delta(S,K,T,r,sigma):
    d1_value = d1(S,K,T,r,sigma)
    delta_call = norm.cdf(d1_value)
    return delta_call


def put_delta(S,K,T,r,sigma):
    d1_value = d1(S, K, T, r, sigma)
    delta_put = norm.cdf(d1_value) - 1
    return delta_put


def gamma(S,K,T,r,sigma):
    d1_value = d1(S,K,T,r,sigma)

    gamma_value = math.exp(((-(d1_value)**2))/2)/(S*sigma*math.sqrt(2*math.pi))
    return gamma_value


def vega(S,K,T,r,sigma):
    d1_value = d1(S,K,T,r,sigma)
    N_of_d1 = math.exp((((-(d1_value)**2))/2))/math.sqrt(2*math.pi)

    vega_value = S*math.sqrt(T)*N_of_d1
    return vega_value
