#Sieve of Eratosthenes
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

"""
prime_list = [
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 
        31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 
        73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 
        127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 
        179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 
        233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 
        283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 
        353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 
        419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 
        467, 479, 487, 491, 499, 503, 509, 521, 523, 541,
        547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 
        607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 
        661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 
        739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 
        811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 
        877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 
        947, 953, 967, 971, 977, 983, 991, 997
]
"""

# This was the first method I tried where I attempted to generate all permuations with brute force
# This proved to be much too slow, so we need to resort to Dynamic Programming
# It also doesn't work...so there's that
"""
def cross_lists(A, B):
    return [A[i]+B[j] for i in range(len(A)) for j in range(i, len(B))]

# This was a good first try, but it's too slow to check every number individually
def prime_sums(n):
    
    cnt = 0
    sums = list(prime_list)
    while sums != []:
        for s in sums:
            if s == n:
                cnt += 1

        sums = list(filter(lambda x: x < n, sums))
        sums = cross_lists(prime_list, sums)

    return cnt

prime_list = Sieve(1000)
max_sum = 0
max_i = 0
i = 0
while max_sum < 10:
    s = prime_sums(i)
    if s > max_sum:
        max_sum = s
        max_i = i
    print i, s
    i += 1

print
print "DONE"
print
print max_i, max_sum
"""

# We just need to modify the previous method slightly
#   This utilizes a recursive relation: how can obtain the prime partition of n given all the prime partitions less than n?
#   Let's ananlyze the case of n = 10
#       7 | + 3                     = # of ways to prime partition 3 with primes <= 7
#       5 | + 5                     = # of ways to prime partition 5 with primes <= 5
#       5 | + 3 + 2
#       3 | + 3 + 2 + 2             = # of ways to prime partition 7 with primes <= 3
#       2 | + 2 + 2 + 2 + 2         = # of ways to prime partition 8 with primes <= 2
#
#   If we define a new function P(n, pk) = number of ways to partition to partition n with numbers <= pk, where pk is the kth prime then
#               P(n) = SUM{ P(n-pk, pk) } for pk = primes < n
#   now we make an algorithm to exploit this

def P(n):    
    
    prime_list = Sieve(n)
    partitions = [0]*(n+1)
    partitions[0] = 1
    
    for i in range(0, len(prime_list)):
        for j in range(prime_list[i], n+1):
            partitions[j] += partitions[j - prime_list[i]]

    partitions[0] = 0
    return partitions

n = 2
N = 5000
while P(n)[-1] < N:
    n += 1
p = P(n)
print p
print "Lowest number that can be prime partitioned in over", N, "ways", n
