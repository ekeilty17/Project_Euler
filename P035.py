def isPrime(n):
    if n <= 0:
        return False
    if n == 1:
        return False
    first_few = [      2,   3,   5,   7,  11,  13,  17,  19,  23,  29,  31,  37,  41,  43,  47,
                      53,  59,  61,  67,  71,  73,  79,  83,  89,  97, 101, 103, 107, 109, 113,
                     127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]
    if n in first_few:
        return True
    for i in range(2,int(n**(0.5))+1):
        if n % i == 0:
            return False
    return True

def numDigits(n):
    cnt = 0
    while n != 0:
        n /= 10
        cnt += 1
    return cnt

def rotate(n):
    one = n%10
    d = numDigits(n)
    n /= 10
    n += one*(10**(d-1))
    return n

def isCircular(n):
    d = numDigits(n)
    for i in range(0,d):
        if not isPrime(n):
            return False
        n = rotate(n)
    return True

"""
#generate the list of the first million primes
primes = []
for i in range(2,1000000):
    if isPrime(i):
        primes += [i]
"""

out = []
for i in range(0, 1000000):
    if isCircular(i):
        out += [i]


print out
print len(out)
