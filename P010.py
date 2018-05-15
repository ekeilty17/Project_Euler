import math

def isPrime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n == 3:
        return True
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True
"""
accum = 0
for i in range(0,2000000):
    if isPrime(i):
        print i
        accum += i
"""
#this works, but it's really ineffient
#let's try to optimize

accum = 0
for i in xrange(3,2000000,2):
    if isPrime(i):
        print i
        accum += i

print accum
