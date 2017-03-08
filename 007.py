# 007.py
# What is the 10 001st prime number?

from pyler_tools import eratosthenes

def nth_prime(n):
    count = 1
    for prime in eratosthenes():
        if count == n:
            return prime
        count += 1

def main():
    print(nth_prime(10001))

if __name__ == '__main__':
    main()
