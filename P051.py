def Sieve(n):
    #Error Check
    if type(n) != int and type(n) != long:
        raise TypeError("must be integer")
    if n < 2:
        raise ValueError("must be greater than one")
    sieve = [True] * (n+1)
    prime_list = []
    for i in xrange(2,n+1):
        if sieve[i]:
            prime_list += [i]
            #this for loop is analogous to crossing out
            #all multiples of a number in a given range
            for j in xrange(i, n+1, i):
                sieve[j] = False
    return prime_list

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

def getDigit(N,n):
    for i in range(0,n-1):
        N /= 10
    return N%10

def replaceDigit(N,d,n):
    if numDigits(N) < n:
        return N
    return N - getDigit(N,n)*(10**(n-1)) + d*(10**(n-1))

primes = Sieve(1000000)

def stuff():
    for p in primes:
        print p
        N = numDigits(p)
        #i,j,k are indexes of the digits being replaced
        #exclude frst digit bc can't be even
        for i in range(2,N-1):
            for j in range(i+1,N):
                #exclude last digit bc can't start with zero
                for k in range(j+1,N+1):
                    cnt = 0     #counter for number of primes in the family
                    for d in range(0,10):
                        #so we can't replace the leftmost digit with a zero...it's just not allowed
                        if k != N+1 and d != 0:
                            q = replaceDigit(p,d,i)
                            q = replaceDigit(q,d,j)
                            q = replaceDigit(q,d,k)
                            if isPrime(q):
                                cnt += 1
                            print q
                        #a break case to make it more efficient
                        if cnt + (10-d) < 8:
                            break
                    if cnt == 8:
                        return p,i,j,k
                    print

print stuff()
