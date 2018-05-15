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

mx_n = 1000000
n = 1000000
primes = Sieve(n)

mx_len = 0
mx_run = []
mx_accum = 0

for i in range(0,len(primes)):
    accum = primes[i]
    for j in range(i+1,len(primes)):
        if accum > mx_n:
            break
        if j != i+1 and isPrime(accum):
            print primes[i],"to",primes[j-1],"equals",accum
            if j-i > mx_len:
                mx_len = j-i
                mx_run = [primes[i], primes[j-1]]
                mx_accum = accum
        accum += primes[j]
    if len(primes)-i < mx_len:
        break
    else:
        print

print
print mx_len,mx_run,mx_accum
