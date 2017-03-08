# 010.py
# Find the sum of all the primes below two million.

from pyler_tools import eratosthenes

def main():
    S = 0
    for prime in eratosthenes():
        if prime < 2000000:
            S += prime
        else:
            break
    print(S)

if __name__ == '__main__':
    main()
