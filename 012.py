# 012.py
# What is the value of the first triangle number to have over five hundred
# divisors?

from pyler_tools import eratosthenes
from itertools import count

def prime_factorization(N):
    factors = []
    count = 0
    for prime in eratosthenes():
        if N == 1:
            break
        while N % prime == 0:
            N = N / prime
            count = count + 1
        factors.append((prime,count))
        count = 0
    return factors

def main():
    for n in count(8): # we are given the factors up to n = 7
        T = (n*(n+1))/2 # get nth triangle number
        product = 1
        for factor in prime_factorization(T):
            if factor[1] != 0:
                product = product * (factor[1] + 1)
        if product > 500:
            print("%s has %s divisors." % (T, product))
            break

if __name__ == '__main__':
    main()
