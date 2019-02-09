def Prime_Factors(n, limit=1000000):
    #Error Check
    if type(n) != int and type(n) != long:
        raise TypeError('must be integer')
    if n < 2:
        return []
    factors = []
    #as always, take care of the 2s first bc they are easy
    while n % 2 == 0:
        factors += [2]
        n /= 2
    #if n was purely a power of 2, then the function ends here
    if n == 1:
        return factors
    #since we got rid of the 2's potential factors, f, can start at 3
    #other than that, this loop is pretty self explanatory
    f = 3
    while f*f <= n:
        if limit < f:
            raise OverflowError('limit exceeded')
        if n % f == 0:
            factors += [f]
            n /= f
        else:
            f += 2
    return factors + [n]

#If n is prime, phi(n) = n-1
#If m and n are coprime, phi(n*m) = phi(n)*phi(m)
#If a and n are coprime, a^phi(n) % n = 1
def phi(n):
    if n < 1:
        return -1
    if n == 1:
        return 0
    f = list(set(Prime_Factors(n)))
    accum = n
    for p in f:
        accum *= (1 - 1/float(p))
    return int(accum)

def getDigits(n):
    out = []
    while n != 0:
        out = [n%10] + out
        n /= 10
    return out

def isPermutation(n, m):
    return sorted(getDigits(n)) == sorted(getDigits(m))    


mn = 2/float(phi(2))
mn_n = 2
for n in range(2,10**7):
    p = phi(n)
    if isPermutation(n, p):
        print n,p, n/float(p), mn, mn_n
        if n/float(p) < mn:
            mn = n/float(p)
            mn_n = n

print mn,mn_n
# I kinda brute forced ths one
# I don't know if it's bc my primes factors function is too slow 
# or if there is a way improve the phi function for this specific problem 
