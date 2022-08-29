import math
from itertools import permutations
from collections import defaultdict

# The first observation is that there are 3 candidates of the shortest path, 
# which correspond to the 3 combinations of faces that we can take (x, y), (y, z), or (z, x)
#
# If we fix the two faces we are going to travel along, the shortest path becomes an optimization problem
# we have to find the point at the intersection of those two faces, that gives the shortest distance
# to do this, we just do a little bit of calculate of the distance formula 
def shortest_path(a, b, c):

    # this is the distance formula from point (0, 0, 0) --> (x, 0, c) --> (a, b, c)
    def dist(a, b, c, x):
        return math.sqrt(c**2 + x**2) + math.sqrt((a-x)**2 + b**2)

    # you can plug in x_opt into dist() and do some algebra to show it reduces to this
    def opt_distance(a, b, c):
        return math.sqrt(a**2 + (b + c)**2)

    # if you take the derivative and set it to zero, you would get the formula for x_opt 
    # you can do that for the other two permutations of the sides to get y_opt and z_opt
    x_opt = (a*c) / (b + c)
    y_opt = (a*b) / (a + c)
    z_opt = (b*c) / (a + b)

    # we then return the minimum of these three options
    candidates = [dist(a, b, c, x_opt), dist(b, c, a, y_opt), dist(c, a, b, z_opt)]
    SP = min(candidates)
    return SP


# In fact, you can prove that the shortest distance always occurs when you take (a, b, c) in reversed sorted order
# if we let the function assume that a >= b >= c, coupled with the simplified formula for dist()
# this just becomes a one-line function
# we return the square of the shortest path for numerical stability
def shortest_path_squared_optimized(a, b, c):
    a, b, c = tuple(reversed(sorted([a, b, c])))
    return a**2 + (b + c)**2

def isPerfectSquare(n):
    s = math.sqrt(n)
    return math.floor(s)**2 == n or math.floor(s)**2 == n

# Given max dimension size MxMxM, this calculates the number of integer shortest paths
def integer_shortest_paths_naive(M):
    total = 0
    for c in range(1, M+1):
        for b in range(c, M+1):
            for a in range(b, M+1):
                # Note that a <= b <= c
                #print(a, b, c)

                """
                # another way of doing it, but not as numerically stable
                SP_squared = shortest_path(a, b, c)
                SP = round(SP, 10)      # this is to deal with numerical errors
                                        # you can get stuff like 18.0000000001 or 17.99999999
                if SP == int(SP):
                    total += 1
                """

                SP_squared = shortest_path_squared_optimized(a, b, c)
                if isPerfectSquare(SP_squared):
                    total += 1
    return total


# We convert the above function into a search for when the number of integer shortest paths exceeds N
# Works, but is way too slow. We need a different appraoch
def brute_force(N):

    total = 0
    M = 1
    while total < N:
        print(M-1, total)

        # we imagine that in previous iterations we've checked all cuboids within the dimensions (m x m x m)
        # now we want to get all (m+1) x (m+1) x (m+1) cuboids
        a = M
        for b in range(1, a+1):
            for c in range(1, b+1):
                # Note that a >= b >= c
                #print(a, b, c)

                SP_squared = shortest_path_squared_optimized(a, b, c)
                if isPerfectSquare(SP_squared):
                    total += 1
        M += 1
    return M-1


# We know that if a <= b <= c, then the shortest path is given by sqrt(a^2 + (b+c)^2)
# so we can transform the problem into finding pythagorean triples x^2 + y^2 = z^2
# with x=a and y=b+c (value of z doesn't matter as long as it's an integer)
#
# So, we can just find all pythagorean triples subject to x <= M and y <= 2M
# and then just count the number of ways we can split y = b+c such that b, c <= M
def integer_shortest_paths_pythagorean_triples(M):
    total = 0
    for x in range(1, M+1):
        for y in range(x, 2*M+1):
            z_squared = x**2 + y**2
            if isPerfectSquare(z_squared):      # this means it's an integer path
                z = int(math.sqrt(z_squared))
                total += count_integer_paths(x, y, M)
    return total

# we have this as a separate function because we use it again later
# Note that (x, y) is assumed to be the legs of an integer pythagorean triple
def count_integer_paths(x, y, M):
    total = 0
        
    # if we let a=x, 
    # so we need to determine all y = b+c such that we still maintain a <= b <= c and b, c <= M
    if x > (y-1)//2:
        total += (x - (y-1)//2)

    # if we let a=y, we we need to find a^2 + (b+c)^2 = k^2
    # so we need to determine all x = b+c such that we still maintain a <= b <= c and b, c <= M
    if y <= M:
        total += (x//2)
    
    return total

# Just as before, we convert the function for a specific MxMxM dimension into a search
def counting_pythagorean_triples(N):

    triples = set()
    total = 0
    M = 1
    while total < N:
        # These two for loops are essentially just getting the new pythagorean triples for the increased M
        for x in range(1, M):
            for y in range(2*(M-1)+1, 2*M+1):
                z_squared = x**2 + y**2
                if isPerfectSquare(z_squared):
                    z = int(math.sqrt(z_squared))
                    triples.add((x, y, z))
        
        x = M
        for y in range(M, 2*M+1):
            z_squared = x**2 + y**2
            if isPerfectSquare(z_squared):
                z = int(math.sqrt(z_squared))
                triples.add((x, y, z))

        # we need to recalculate the number of integer paths of each pythagorean triple 
        # because as M increases, the number of ways to split y = b+c changes
        # There may be a more efficient way, but this is fast enough
        total = sum([count_integer_paths(x, y, M) for x, y, _ in triples])
        M += 1

    return M-1


# TODO: There are definately more efficient ways to get all the pythegorean triples,
#       also there is still some redundant computation when getting the new total
#       but I've been working on this problem for too long, and this solution is fast enough for me

def main(N=10**6):
    M = counting_pythagorean_triples(N)
    print(f"The least value of M such that the number of solutions first exceeds {N} is:", M)
    return M

if __name__ == "__main__":
    main()