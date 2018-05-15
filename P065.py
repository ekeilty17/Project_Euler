def sumDigits(n):
    accum = 0
    while n != 0:
        accum += n%10
        n /= 10
    return accum

def gcd(a, b):
    if b > a:
        a, b = b, a
    while b != 0:
        a, b = b, a%b
    return a

#takes a list and produces the continued fraction
def ContinuedFraction_dec(L):
    accum = L[-1]
    for i in range(len(L)-2,-1,-1):
        accum = L[i] + 1/float(accum)
    return accum


def ContinuedFraction_frac(L):
    #accum = [a,b] where e ~ a/b
    accum = [L[-1], 1]
    for i in range(len(L)-2,-1,-1):
        a = accum[0]
        b = accum[1]
        accum[0] = L[i]*a + b
        accum[1] = a
        #you actually don't need this bc they will always be relatively prime
        #g = gcd(accum[0],accum[1])
        #accum[0] /= g
        #accum[1] /= g
    return accum

def gen_e_list(n):
    out = []
    for i in range(1,(n//3)+2):
        out += [1,2*i,1]
    if n%3 == 2:
        out = out[:-1]
    elif n%3 == 1:
        out = out[:-2]
    else:
        out = out[:-3]
    return [2] + out

def e_approx_dec(n):
    return ContinuedFraction_dec(gen_e_list(n))

def e_approx_frac(n):
    return ContinuedFraction_frac(gen_e_list(n))


n = 100
print gen_e_list(n-1)
L = e_approx_frac(n-1)
print L
print L[0]/float(L[1])
print sumDigits(L[0])
