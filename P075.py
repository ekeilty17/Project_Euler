import math
from collections import defaultdict

def isPerfectSquare(n):
    s = math.sqrt(n)
    return math.floor(s)**2 == n or math.floor(s)**2 == n


# brutally slow
def brute_force(N):

    triples = defaultdict(set)

    for a in range(1, N+1):
        for b in range(a, N+1):
            #print(a, b)
            c_squared = a**2 + b**2
            c = int(math.sqrt(c_squared))
            L = a + b + c
            if L > N:
                break
            if isPerfectSquare(c_squared):
                triples[L].add( (a, b, c) )
    
    #number_of_triples_per_integer = [len(triples[L]) for L in range(N+1)]
    for L in sorted(triples):
        print(L, triples[L])
    return len([L for L in triples if len(triples[L]) == 1])
            


# Basically we have to find a way to generate all pythagorean triples
# Using a video from 3Blue1Brown https://www.youtube.com/watch?v=QJYmyhnaaek&t=455s
#       We notice that (u + iv) * (u - iv) = (u^2 - v^2) + (2uv)i
#       and this forms a right-triangle in the 2d complex plane
# It turns out this formula will generate non-trivial pythagorean triples from any two distinct integers
#       i.e. let u > v, then (u, v) --> (u^2 - v^2, 2uv)
def Dickson_method(N):
    # create a list with indeces corresponding to the total length of the wire
    # and elements corresponding to a set of the possible hypotenuses of triangles that can be formed by the wire
    triples = defaultdict(set)

    # for a given (u, v)
    # L = a + b + c = (u^2 - v^2) + (2uv) + (u^2 + v^2) = 2u^2 + 2uv
    # Therefore, N >= L > 2u^2 --> u < sqrt(N/2)
    upper_u = math.ceil(math.sqrt(N/2))
    for u in range(1, upper_u+1):
        
        # since u > v, u is our upper bound for v
        # Note that u = v does not produce a triangle
        for v in range(1, u):
            #print(u, v)
            
            # breaking condition
            a, b, c = u**2 - v**2, 2*u*v, u**2 + v**2
            a, b = min(a, b), max(a, b)
            L = a + b + c
            if L > N:
                break
            
            # to get multiples of the non-trivial pythagorean triples
            # for example:  (3, 4, 5) --> (6, 8, 10) --> (9, 12, 15) --> etc
            # we use sets because we only care about the number of unique entries
            k = 1
            while k * L <= N:
                triples[k * L].add( (k*a, k*b, k*c) )
                k += 1

    #for L in sorted(triples):
    #    print(L, triples[L])
    return len([L for L in triples if len(triples[L]) == 1])


def main(N=1500000):

    #total = brute_force(N)
    total = complex_multiplication_method(N)

    print(f"How many integer right-triangles can be formed from a wire of length L <= {N} is:", total)
    return total

if __name__ == "__main__":
    main()