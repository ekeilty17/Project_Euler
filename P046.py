def Sieve(n):
    #Error Check
    if type(n) != int and type(n) != long:
        raise TypeError("must be integer")
    if n < 2:
        raise ValueError("must be greater than one")
    sieve = [True] * (n+1)
    prime_list = []
    odd_composite = []
    for i in xrange(2,n+1):
        if not sieve[i] and i%2 == 1:
            odd_composite += [i]
        if sieve[i]:
            prime_list += [i]
            #this for loop is analogous to crossing out
            #all multiples of a number in a given range
            for j in xrange(i, n+1, i):
                sieve[j] = False
    return [prime_list, odd_composite]

L = Sieve(100000)
primes = L[0]
odd_comp = L[1]
squares = [x*x for x in range(1,int((odd_comp[-1]/2)**0.5)+2)]

print squares

sums = []
for n in odd_comp:
    found = False
    p = 0
    #print n
    while p < len(primes) and primes[p] < n:
        s = 0
        while s < len(squares) and 2*squares[s] < n:
            if n == primes[p] + 2*squares[s]:
                print n,"=",primes[p],"+ 2 x",squares[s]
                found = True
                p = len(primes)
                s = len(squares)
            s += 1
        p += 1
    if not found:
        print
        print n
        break
