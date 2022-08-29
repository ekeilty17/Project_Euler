from collections import defaultdict
import itertools
import math

def getDigits(n):
    return [int(d) for d in str(n)]

# For a given permutation of digits, the largest it can be is the digits sorted from largest to smallest
# so we just need to check that for all cubes between n**3 and this upperbound, none of these contain the same permutation of digits
def check_remaining_cubes(digits, n):
    digits = list(sorted(digits))
    upper_bound = int( "".join([str(d) for d in reversed(digits)]) )
    while n**3 <= upper_bound:
        if tuple(sorted(getDigits(n**3))) == digits:
            return False
        n += 1
    return True

# we just iterate through each cube and keep a dictionary indexed by its digits
# if two numbers have the same set of digits, they will index into the same slot in the dictionary
# once we get a list of size N, then we have found the desired set of cubes
def brute_force(N):

    cubes = defaultdict(list)
    n = 1
    while True:
        ordered_digits = tuple(sorted(getDigits(n**3)))
        cubes[ordered_digits].append(n)

        if len(cubes[ordered_digits]) == N:
            # The question says it needs to be exactly N, 
            # so we need to check that no other permutations produce perfect cubes
            if check_remaining_cubes(ordered_digits, n):
                return cubes[ordered_digits]
        
        n += 1

def main(N=5):

    cubes = brute_force(N)
    #print([(m, m**3) for m in cubes])

    min_cube = min(cubes)**3
    print(f"The smallest cube for which exactly {N} permutations of its digits are cube is:", min_cube)
    return min_cube

if __name__ == "__main__":
    main()