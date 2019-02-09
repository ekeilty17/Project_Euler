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
L = list_fract(8)
print 8
x = [s[1:] for s in L]
print x

"""

#instead I think the strategy is to zoom in on 3/7
def list_fract_ab(a, b, limit):
    #want to find the few fractions before a/b
    #in this case a = 3, b = 7
    out = []
    for denom in range(2,limit+1):
        #say we want to know which is bigger, numer/denom or a/b
        #use the trick if numer/denom > a/b, then number*b > denom*a
        start = 0
        while start*b < denom*(a-1):
            start += 1
        start -= 1
        end = start
        while end*b < denom*a:
            end += 1
        print denom, start, end
        start += 1
        if end == 0:
            continue
        
        #now it should always be the case that
        #   (a-1)/b < numer/denom < a/b
        for numer in range(start,end):
            out += [[numer/float(denom), numer, denom]]
    return list(sorted(out))

"""
L = list_fract_ab(1000,3,7)
print L
print
x = [s[1:] for s in L]
print x
print
print x[-1]
"""

# This problem is actually a searching problem...listing is far too slow
# we loop through all denominators and want to find the corresponding numerator that is the closest to 3/7 without going over
# we get an upper and lower bound for this numerator using
#   lower = floor(3/7) * denominator = 0
#   upper = ceiling(3/7) * denominator = denominator
# and we do a binary search in order to find x such that x/denominator is the closest to 3/7
def nearest_frac(a, b, limit):
    nearest = [0, 1]
    for denom in xrange(2, limit+1):
        # we want to get an estimate for a fraction with a denominator of 'denom'
        lower = a/b * denom
        upper = (a/b + 1)*denom
        # doing a binary search to find closest fraction
        # I was doing a linear search before and that was far too slow
        while lower != upper-1:
            mid = lower + (upper - lower)/2
            if mid/float(denom) < a/float(b):
                lower = mid
            else:
                upper = mid
        # updating nearest fraction
        if lower/float(denom) > nearest[0]/float(nearest[1]):
            nearest = [lower, denom]
            print a/float(b), nearest, lower/float(denom)
    return nearest

print nearest_frac(3, 7, 1000000)
