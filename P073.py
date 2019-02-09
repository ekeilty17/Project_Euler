def gcd(a, b):
    #accounting for this annoying case
    if b > a:
        a, b = b, a

    #gcd(a,b) = gcd(b,a%b) --> Euclid's Algorithm
    while b != 0:
        a, b = b, a%b
    return a

#slow way
def list_fract_between(f1, f2, limit):
    out = []
    #out = [ [dec, numer, denom], [...], ... ]
    for denom in range(2,limit+1):
        print denom
        lower = f1[0]/float(f1[1]) * denom
        upper = (f2[0]+1)/float(f2[1]) * denom
        for numer in range(int(lower),int(upper)+1):
            if gcd(numer, denom) == 1:
                out += [[numer/float(denom), numer, denom]]
    return list(sorted(out))

L = list_fract_between([1,3], [1,2], 12000)
# just cleaning up the list
L = [x[1:] for x in L]
# extracting part we care about
L = L[L.index([1,3])+1: L.index([1,2])]
print
print len(L)

# The above works but it takes forever for python to get the length of the list produced cuz it's so big
# There are a myriad of ways you could make the code more efficient even still maintaining this method
#   For example you could do it in chunks so python doesnt have to store such a massive list
# You could also use the code from P071.py in order to find the numerator value associated with the denominator that was just above and just below 1/3 and 1/2 and then you never even have to generate a list
