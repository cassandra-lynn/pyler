# 006.py
# Find the difference between the sum of the squares of the first one hundred
# natural numbers and the square of the sum.

def main():
    print( sum([n for n in range(101)])**2 - sum([n**2 for n in range(101)]))

if __name__ == '__main__':
    main()
