# Basically we have to find a way to generate all pythagorean triples
# Using a video from 3Blue1Brown https://www.youtube.com/watch?v=QJYmyhnaaek&t=455s
# This formula will generate non-trivial pythagorean triples from any two distinct integers
#   (u,v) --> (u**2 - v**2, 2*u*v)

# generate a non-trivial pythagorean triple from any pair of integers
def f(t):
    u = max(t[0], t[1])
    v = min(t[0], t[1])
    # (a, b, c)
    return (u**2 - v**2, 2*u*v, u**2 + v**2)

# create a list with indeces corresponding to the total length of the wire
# and elements corresponding to a set of the possible hypotenuses of triangles that can be formed by the wire
limit = 1500000
L = [None]*(limit+1)

# note: limit/2 is just my estimate for when the loop should end
#       it probably is possible to do this slightly more efficiently with while loops
for a in range(1, limit/2):
    
    # breaking condition
    l = f((a,a+1))
    if sum(l) > limit:
        break
    
    # a = b does not produce an triangle, so we start at a+1 as to not repeat
    for b in range(a+1, limit/2):
        print a,b
        
        # breaking condition
        l = f((a,b))
        if sum(l) > limit:
            break
        
        # to get multiples of the non-trivial pythagorean triples
        # for example:  (3, 4, 5) --> (6, 8, 10) --> (9, 12, 15) --> etc
        # we use sets because we only care about the number of unique entries
        k = 0
        while (k+1)*sum(l) <= limit:
            k += 1
            if L[k*sum(l)] == None:
                L[k*sum(l)] = set()
            L[k*sum(l)].add(k*l[2])

#print L

indeces = []
for i in range(len(L)):
    if L[i] == None:
        continue
    elif len(L[i]) == 1:
        indeces += [i]

#print indeces
print len(indeces)
