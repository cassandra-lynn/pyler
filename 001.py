# 001.py
# Find the sum of all the multiples of 3 or 5 below 1000.

sum=0
for n in range(0,1000):
    if n % 3 is 0 or n % 5 is 0:
        sum = sum + n
print sum
