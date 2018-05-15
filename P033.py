def get_ones(n):
    if n < 10 or n > 99:
        return -1
    return n%10

def get_tens(n):
    if n < 10 or n > 99:
        return -1
    return n/10

def rm_ones(n):
    if n < 10 or n > 99:
        return -1
    return n/10

def rm_tens(n):
    if n < 10 or n > 99:
        return -1
    return n%10

#getting fractions
fracts = []
for numer in range(11,50):
    for denom in range(numer+1,100):
        if numer%10 != 0 and denom%10 != 0:
            if numer/float(denom) == rm_ones(numer)/float(rm_ones(denom)) and get_ones(numer) == get_ones(denom):
                fracts += [[numer,denom]]
            elif numer/float(denom) == rm_tens(numer)/float(rm_ones(denom)) and get_tens(numer) == get_tens(denom):
                fracts += [[numer,denom]]
            elif numer/float(denom) == rm_ones(numer)/float(rm_tens(denom)) and get_ones(numer) == get_tens(denom):
                fracts += [[numer,denom]]
            elif numer/float(denom) == rm_tens(numer)/float(rm_tens(denom)) and get_tens(numer) == get_tens(denom):
                fracts += [[numer,denom]]

print fracts

#multiplying them
numerator = 1
denominator = 1
for f in fracts:
    numerator *= f[0]
    denominator *= f[1]

#finding GCF using Euliers Method
def gcd(a,b):
    if b > a:
        return gcd(b, a)
    if a % b == 0:
        return b
    return gcd(b, a%b)

div = gcd(numerator,denominator)

print numerator, denominator
print numerator/div, denominator/div
