# 003.py
# What is the largest prime factor of the number 600851475143 ?

from itertools import count


def eratosthenes():
    """Yields the sequence of primes via the sieve of eratosthenes."""

    composites = {}
    for query in count(2):
        prime = composites.pop(query, None)
        if prime is None:
            yield query
            composites[query ** 2] = query
        else:
            composite = prime + query
            while composite in composites:
                composite += prime
            composites[composite] = prime

def get_prime_factors(N):
    """Returns a list of the prime factors of N"""

    factors = []
    for prime in eratosthenes():
        if prime > N ** 0.5: break
        if N % prime == 0:
            factors.append(prime)
    return factors

def main():
    target=600851475143
    print(get_prime_factors(target).pop())

if __name__ == '__main__':
    main()
