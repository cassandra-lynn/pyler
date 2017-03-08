# 009.py
# find abc that satisfies a+b+c=1000 and a^2+b^2=c^2

from itertools import count, islice

def stifel():
    """Yields a tuple containing a pythagorean triple.

    According to Michael Stifel, there are an infinite number of pythagorean
    triples of the form [2*(n**2+n), (2*n+1), 2(n**2+n)+1]. This function yields
    a triple of that form."""

    for n in count(1):
        a = 2*(n**2+n)
        b = 2*n+1
        c = a+1
        yield a, b, c

def ozanam():
    """Yields a tuple containing a pythagorean triple.

    Jacques Ozanam added a similar sequence on to Stifel's. Ozanam says there
    are an infinite number of pythagorean triples of the form 
    [(2*n+1)*(2*n+3), 4*(n+1), (2*n+1)*(2*n+3)+2]. This function yields a triple
    of that form."""

    for n in count(1):
        a = (2*n+1)*(2*n+3)
        b = 4*(n+1)
        c = a+2
        yield a, b, c

def greek_trips():
    """Yields a tuple containing a pythagorean triple.

    Pythagoras's formula: a = a, b = (a**2-1)/2, c = (a**2+1)/2 for some odd a
    Plato's formula: a = a, b = (a/2)^2 - 1, c = (a/2)^2 + 1 for some even a"""

    for a in count(1):
        if a % 2 != 0: # Odd: Pythagoras
            yield a, int((a**2-1)/2), int((a**2+1)/2)
        else: # Even: Plato
            yield a, int((a/2)**2-1), int((a/2)**2+1)
            
def euclid(max_m=None, max_n=None):
    """Yields a tuple containing a pythagorean triple.

    for m > n > 0 and m, n int: a = m**2-n**2, b = 2*m*n, c = m**2+n**2"""

    for n in islice(count(1), max_n):
        for m in islice(count(n+1), max_m):
            yield m**2-n**2, 2*m*n, m**2+n**2

def main():
    for triple in euclid(15, 10):
        if sum(triple) == 1000:
            print(triple[0]*triple[1]*triple[2])

if __name__ == '__main__':
    main()
