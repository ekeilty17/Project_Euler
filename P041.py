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

def getDigits(n):
    out = []
    while n != 0:
        out = [n%10] + out
        n /= 10
    return out

def isPandigital(N,n):
    if list(sorted(getDigits(N))) == range(1,n+1):
        return True
    return False


def allPandigital(n):
    if n == 0:
        return [[0]]
    if n == 1:
        return [[1]]
    if n == 2:
        return [[1,2], [2,1]]
    n_1 = allPandigital(n-1)
    out = []
    for sL in n_1:
        for i in range(len(sL),-1,-1):
            out += [ sL[0:i] + [n] + sL[i:] ]
    return out

def numberfy(L):
    accum = 0
    for i in range(0,len(L)):
        accum *= 10
        accum += L[i]
    return accum

#if you run the below with 8 or 9 you will get an empty list
#there are no 8-pandigital or 9-pandigital primes
out = []
pan = allPandigital(7)
for p in pan:
    if isPrime(numberfy(p)):
        print numberfy(p)
        out += [numberfy(p)]
print
print max(out)

#brute force doesnt work
"""
out = []
i = 123456789
while i < 987654322:
    print i
    if isPandigital(i,9):
        if isPrime(i):
            print i
            out += [i]
    i += 1
print
print out
"""
