def gcd(a, b):
    #accounting for this annoying case
    if b > a:
        a, b = b, a

    #gcd(a,b) = gcd(b,a%b) --> Euclid's Algorithm
    while b != 0:
        a, b = b, a%b
    return a

#Too slow
def phi(n):
    if n < 1:
        return -1
    if n == 1:
        return 0
    accum = 1   #starts at 1 bc everything is relatively prime to 1
    for i in range(2,n):
        if gcd(n,i) == 1:
            accum += 1
    return accum

#still too slow, need some thms
def phi_2(n):
    if n < 1:
        return -1
    if n == 1:
        return 0
    #initializing poccessed: the numbers I have already look at/ eliminated
    processed = [False]*(n)
    processed[0] = True
    processed[1] = True
    
    p = 1   #to account for the fact 1 is always relatively prime

    for i in range(2,n):
        if processed[i] == False:
            if gcd(n,i) == 1:
                a = 1
                while i**a < n:
                    a += 1
                for j in range(1,a):
                    processed[i**j] = True
                    p += 1
    return p

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
def phi_3(n):
    if n < 1:
        return -1
    if n == 1:
        return 0
    f = list(set(Prime_Factors(n)))
    accum = n
    for p in f:
        accum *= (1 - 1/float(p))
    return int(accum)
    
mx = 0
mx_n = 0
for n in range(2,1000000):
    p = phi_2(n)
    print n,p
    if n/float(p) > mx:
        mx = n/float(p)
        mx_n = n

print mx,mx_n

