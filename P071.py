#slow way
def list_fract(n):
    out = []
    #out = [ [dec, numer, denom], [...], ... ]
    for denom in range(2,n+1):
        for numer in range(1,denom):
            out += [[numer/float(denom), numer, denom]]
    return list(sorted(out))

"""
L = list_fract(1000)
x = [s[1:] for s in L]
print x
"""

#there is no way the above would work for n = 1 000 000
#instead I think the strategy is to zoom in on 3/7
def list_fract_ab(n,a,b):
    #want to find the few fractions before a/b
    #in this case a = 3, b = 7
    out = []
    for denom in range(2,n+1):
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

L = list_fract_ab(100000,3,7)
x = [s[1:] for s in L]
print x
print
print x[-1]
