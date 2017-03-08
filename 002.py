# 002.py
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

import math

def fib(n):
    phi = (1+math.sqrt(5))/2.0
    return int((phi**n-(-phi)**(-n))/(2*phi-1))

def sum_even_fib(n):
    phi = (1+math.sqrt(5))/2.0
    return (1/math.sqrt(5))*((1-((1+math.sqrt(5))/2)**(3*n+3))/(1-((1+math.sqrt(5))/2)**3-(1-((1-math.sqrt(5))/2)**(3*n+3)))/(1-((1-math.sqrt(5))/2)**3))
    # ^^ this is wrong!!!! i don't know why right now, but i'll figure it out later.

def main():
    n = 1
    while True:
        if fib(n) >= 4000000:
            n = n - 1
            break
        n = n + 1; 
    print(sum_even_fib(n))

if __name__ == '__main__':
    main()
