# pylertools.py
# useful functions for doing project euler problems

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
