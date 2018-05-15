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

#Global Variable
primes = Sieve(1000000)

def Prime_Factors(n):
    if n == 0:
        return [-1]
    if n == 1:
        return [1]

    out = []
    while n != 1:
        for p in primes:
            if n%p == 0:
                out += [p]
                n /= p
                break
    return out

#This works, but it's very slow
"""
c = 4
#initalize cand array
#the list(set(...)) gets rid of repeats in the array
cand = []
for i in range(2,2+c):
    cand += [list(set(Prime_Factors(i)))]

cnt = 4
found = False
while not found:
    found = True
    #rotation
    cand = cand[1:] + [list(set(Prime_Factors(cnt)))]
    cnt += 1

    print cnt-c,cand
    #checking that each number has the same number of factors
    for i in range(0,len(cand)):
        if len(cand[i]) != c:
            found = False

s = ""
for i in range(cnt-c,cnt):
    if i != cnt - 1:
        s += str(i) + ", "
    else:
        s += str(i)

print s
"""

#gonna just streamline ^
n = 4
cnt = 0
i = 2
while cnt < n:
    print i, Prime_Factors(i)
    if len(list(set(Prime_Factors(i)))) == n:
        cnt += 1
    else:
        cnt = 0
    i += 1

s = ""
for j in range(i-n,i):
    if j != i - 1:
        s += str(j) + ", "
    else:
        s += str(j)

print s
