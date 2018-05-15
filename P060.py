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

def concat(a,b):
    return int(str(a) + str(b))

def all_concat(L):
    out = []
    for i in range(0,len(L)-1):
        for j in range(i+1,len(L)):
            out += [concat(L[i], L[j]), concat(L[j], L[i])]
    return out

primes = Sieve(10000)

#so this brute forces it, but we can be more clever than this
#say a and b do not concatinate to a prime, then we can discount iterations c, d, and e bc they will never be solutions
"""
def stuff():
    #know it can't start at 2
    for a in range(1,len(primes)-4):
        for b in range(a+1,len(primes)-3):
            for c in range(b+1,len(primes)-2):
                for d in range(c+1,len(primes)-1):
                    for e in range(d+1,len(primes)):
                        print primes[a],primes[b],primes[c],primes[d],primes[e]
                        L = all_concat([primes[a],primes[b],primes[c],primes[d],primes[e]])
                        cnt = 0
                        for p in L:
                            if isPrime(p):
                                cnt += 1
                            else:
                                break
                        if cnt == len(L):
                            return [primes[a],primes[b],primes[c],primes[d],primes[e]]
"""

#This is still kinda slow but idk how to make it faster
def all_prime(L):
    for p in L:
        if not isPrime(p):
            return False
    return True

def stuff():
    #know it can't start at 2
    for a in range(1,len(primes)-4):
        for b in range(a+1,len(primes)-3):
            for c in range(b+1,len(primes)-2):
                if not all_prime(all_concat([primes[a],primes[b]])):
                    break
                for d in range(c+1,len(primes)-1):
                    if not all_prime(all_concat([primes[a],primes[b],primes[c]])):
                        break
                    for e in range(d+1,len(primes)):
                        if not all_prime(all_concat([primes[a],primes[b],primes[c],primes[d]])):
                            break
                        print primes[a],primes[b],primes[c],primes[d],primes[e]
                        if all_prime(all_concat([primes[a],primes[b],primes[c],primes[d],primes[e]])):
                            return [primes[a],primes[b],primes[c],primes[d],primes[e]]

    return []
L = stuff()
print L
print sum(L)

#old attempt
"""
#Let's try to find a number by just adding it to the original list
#original list: 3, 7, 109, 673

#you know right away it can't be 2, 3, 5, or 7 just from the original list
candidate = 7 #this is the 4th prime
n = 4

all_prime = False
while all_prime == False and candidate < 1000:
    
    candidate = nthPrime(n+1)
    n += 1
    
    #make a list of every concatination
    concat_list = [ concat(3,candidate), concat(candidate,3),
                    concat(7,candidate), concat(candidate,7),
                    concat(109,candidate), concat(candidate,109),
                    concat(673,candidate), concat(candidate,673)
                  ]

    for c in concat_list:
        all_prime = True
        if isPrime(c) == False:
            all_prime = False
            break

print "next prime in the set is",candidate
accum = 3+7+109+673+candidate
print "lowest sum in the set",accum
#turns out this isn't the lowest sum
"""

"""
a = 13
b = 13
c = 13
d = 13
e = 13

p_set = [a,b,c,d,e]

n_a = 6
n_b = 6
n_c = 6
n_d = 6
n_e = 6

n_set = [n_a,n_b,n_c,n_d,n_e]

for i in range(0,len(p_set)-1):
    all_prime = False
    while all_prime == False and p_set[i+1] < 10000:
        
        for j in range(i+1,len(p_set)):
            p_set[j] = nthPrime(n_set[j]+1)
            n_set[j] += 1
    
        #make a list of every concatination
        concat_list = []
        for j in range(0,len(p_set)-1):
            concat_list += [ concat(p_set[j],p_set[j+1]) ]
            concat_list += [ concat(p_set[j+1],p_set[j]) ]

        for p in concat_list:
            all_prime = True
            if isPrime(p) == False:
                all_prime = False
                break

print p_set
"""
