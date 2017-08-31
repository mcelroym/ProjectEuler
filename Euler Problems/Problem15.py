# How many ways can we arrange 20 R's and 20 D's as a string

from math import *

def nCr(n,r):
    return factorial(n) / factorial(r) / factorial(n-r)

print nCr(40, 20)