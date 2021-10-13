from scipy.stats import norm
import pandas as pd
from pandas_datareader import data as wb
import numpy as np
import matplotlib.pyplot as plt

#BLACK SCHOLES METHOD

# Define Variables
# 1. Interest Rate
r = 0.00
# 2 Underlying product
S = 121.5
# 3 Strike Price
K = 125
# Maturity
T = 90 / 365
# Volatility
sigma = 0.30
# Funtion for BlackScholes
def blackS(r, S, K, T, sigma, type="C"):
    #"Calculate BS option price for a call or put option"
    d1 = (np.log(S/K) + (r + sigma ** 2/2)*T) / (sigma*np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)
    "Now we must decide is this call or put"
    try:
        if type == "C":
            price = S*norm.cdf(d1, 0, 1) - K*np.exp(-r * T)*norm.cdf(d2, 0, 1)
        elif type == "P":
            price = K*np.exp(-r*T)*norm.cdf(-d2, 0, 1) - S*norm.cdf(-d1, 0, 1)
        return price
    except:
        print("Check your parameters in case of misspellings or erros")

print("Option Price is: ", round(blackS(r, S, K, T, sigma, type="C"), 2))
