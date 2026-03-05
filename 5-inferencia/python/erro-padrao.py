import numpy as np
from scipy.stats import norm

print("--------- calculating the prob of only 1 person has IQ > 110")

x=110
media=100
std=15

prob = 1 - norm.cdf(x,media,std) # inverting P(X>100) to 1 - P(X<110)
prob = round(prob,4)

print("Prob: ", prob)

print("--------- calculating the prob of a group of 10 people has IQ > 110")

n = 10
erro_padrao = std/np.sqrt(n)

prob = 1 - norm.cdf(x,media,erro_padrao) # inverting P(X>100) to 1 - P(X<110)
prob = round(prob,4)

print("Prob: ", prob)

print("--------- calculating the prob of a group of 20 people has IQ > 110")

n = 20
erro_padrao = std/np.sqrt(n)

prob = 1 - norm.cdf(x,media,erro_padrao) # inverting P(X>100) to 1 - P(X<110)
prob = round(prob,4)

print("Prob: ", prob)
