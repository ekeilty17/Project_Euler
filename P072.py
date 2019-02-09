from itertools import combinations

def gcd(a, b):
    #accounting for this annoying case
    if b > a:
        a, b = b, a

    #gcd(a,b) = gcd(b,a%b) --> Euclid's Algorithm
    while b != 0:
        a, b = b, a%b
    return a

#slow way
def list_fract(n):
    out = []
    #out = [ [dec, numer, denom], [...], ... ]
    for denom in range(2,n+1):
        for numer in range(1,denom):
            if gcd(numer, denom) == 1:
                out += [[numer/float(denom), numer, denom]]
    return list(sorted(out))


"""
L = list_fract(36)
for e in L:
    print e[1:]
print
print "number of elements:",len(L)
"""

# I think the idea is to start with the maximum possible value and subtract all non-reduced improper fractions
# First off, the max we would start off with is 1 + 2 + 3 + ... + n-1, 
#   which would give us the total number of possible fractions that can be written that are less than 1 
#   and with a denominator less than or equal n
#   This is given by the triangle numbers T(n-1) = (n-1)(n)/2
# Next, we need to determine the prime factors for each denominator. 
#   This will tell us the number we need to subtract off from the total
#   Each prime factor (p) produces (denominator/p-1) numbers that will reduce
# The tricky part is you will double count a reducable fraction if the numerator is also a multiple of the prime factors
#   for example: 6/12 will be counted by the 2 prime factor and the 3 prime factor
#   it's not the most elegant solution, but if you create a list of all possible combinations of the prime factors
#       for example: 60 = 2*2*3*5 --> [[2, 3, 5], [6, 10, 15], [30]]
#   And do then do total += (-1)**(index+1)*(denominator/p-1) you will get the right answer

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

def all_combinations(A):
    out = [A]
    for i in range(2, len(A)+1):
        temp = list(combinations(A, i))
        # a fancy way of multiplying everything in the tuples together
        out += [[reduce(lambda x, y: x*y, t) for t in temp]]

    return out

def num_reduced_improper_fractions(n):
    total = (n-1)*n/2
    
    for denom in xrange(2, n+1):

        PF = list(set(Prime_Factors(denom))) 
        all_factors = all_combinations(PF)
        mult = -1
        for s in all_factors:
            for f in s:
                if f > denom:
                    continue
                total += mult*(denom/f - 1)
                #print denom, f, mult*(denom/f - 1)
            mult *= -1
        
        print denom, total
        
    return total

print num_reduced_improper_fractions(1000000)
