# 004.py
# Find the largest palindrome made from the product of two 3-digit numbers.

from itertools import count

def big_palindrome():
    big = 0
    for x in count(999, -1):
        if x < 100: break
        for y in count(999, -1):
            if y < 100: break
            if str(x*y) == str(x*y)[::-1] and x*y > big:
                big = x*y
    return big

def main():
    print(big_palindrome())

if __name__ == '__main__':
    main()
