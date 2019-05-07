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


N = 5 * 10**7
p = Sieve(10000)

"""
# Too inefficient
for i in p:
    for j in p:
        for k in p:
            print i, j, k
            if i**2 + j**3 + k**4 < N:
                cnt += 1
"""

i = 0
j = 0
k = 0
cnt = 0
nums = set([])
while p[i]**2 + p[j]**3 + p[k]**4 < N:
    while p[i]**2 + p[j]**3 + p[k]**4 < N:
        while p[i]**2 + p[j]**3 + p[k]**4 < N:
            print p[i], p[j], p[k]
            if p[i]**2 + p[j]**3 + p[k]**4 not in nums:
                cnt += 1
                nums.add(p[i]**2 + p[j]**3 + p[k]**4)
            k += 1
        j += 1
        k = 0
    i += 1
    j = 0
    k = 0

print
print cnt
