import itertools

# Polygonal Numbers
def P(k, n):
    if k == 3:
        return (n*(n+1)) // 2       # Triangle
    elif k == 4:
        return n*n                  # Square
    elif k == 5:
        return (n*(3*n-1)) // 2     # Pentagonal
    elif k == 6:
        return n*(2*n-1)            # Hexagonal
    elif k == 7:
        return (n*(5*n-3)) // 2     # Heptagonal
    elif k == 8:
        return n*(3*n-2)            # Octagonal
    else:
        return 0

def get_all_d_digit_polynomal_numbers(N, d):
    all_polygonal_numbers = [[] for k in range(N)]
    for k in range(3, N+3):
        n = 1
        p = P(k, n)
        while p < 10**d:
            if p >= 10**(d-1):
                all_polygonal_numbers[k-3].append(p)
            n += 1
            p = P(k, n)
    
    return all_polygonal_numbers

def get_first_two_digits(n):
    return n // 100

def get_last_two_digits(n):
    return n % 100

# This function assumes that each digit in S is a 4-digit number
# What is confusing about this question is their definition of "cyclic"
# In this question, cyclic means that, for example, in a set of size 6 we have
#   ABCD --> CDEF --> EFGH --> GHIJ --> IJKL --> KLAB
# i.e. we always loop in groups of 2 digits
# 
# In testing this function out it's clear that it's eay too slow to use many times
def isCyclicSet(S):
    for perm in itertools.permutations(S[1:]):
        for i in range(len(perm)-1):
            if get_first_two_digits(perm[i]) != get_last_two_digits(perm[i+1]):
                break
        else:
            # This only occurs if we don't break
            if get_first_two_digits(S[0]) == get_last_two_digits(perm[0]) \
            and get_first_two_digits(perm[-1]) == get_last_two_digits(S[0]):
                return True
    return False

def brute_force(N):
    all_polygonal_numbers = get_all_d_digit_polynomal_numbers(N, 4)

    cyclic_sets = []
    for combination in itertools.product(*all_polygonal_numbers):
        if isCyclicSet(combination):
            cyclic_sets.append(combination)

    return cyclic_sets

def DFS(N, cycle=None, candidates=None):
    # This only runs once and sets up the depth-first search
    if cycle is None:

        # Candidates is a list of lists contain each of the 4-digit polygon numbers
        # The reason we need to keep them separated is because we can only pick one number from each list
        candidates = get_all_d_digit_polynomal_numbers(N, 4)
        remaining = candidates[:-1]

        # output list
        cyclic_sets = []

        # The cycle has to start somewhere, so we will assume the first number comes from the last list
        # This is because the last list is the highest polygon list, which means is will be the shortest
        for first in candidates[-1]:
            cycle = [first]
            # we search for a cycle starting at ``first``
            found, cycle = DFS(N, cycle=cycle, candidates=remaining)
            # if one is found, then we stop and return the cycle
            if found:
                cyclic_sets.append(tuple(cycle))
            # otherwise, we continue to the next number in ``candidates[-1]``

        return cyclic_sets


    # base case: if we get a cycle of length N, then we are done 
    # and we just need to check that the property holds for the first and last numbers in the cycle as well
    if len(cycle) == N:
        first, last = cycle[0], cycle[-1]
        if get_last_two_digits(last) == get_first_two_digits(first):
            return True, cycle
        else:
            return False, cycle
    
    
    # This is the DFS search
    curr = cycle[-1]
    for i in range(len(candidates)):
        remaining = candidates[:i] + candidates[i+1:]
        for nxt in candidates[i]:
            # if we find a number that could be the next on the cycle
            if get_last_two_digits(curr) == get_first_two_digits(nxt):
                # we recurse on that number
                found, new_cycle = DFS(N, cycle=cycle + [nxt], candidates=remaining)
                # if it results in a valid cycle
                if found:
                    # we return
                    return True, new_cycle
    
    # if we fail to find anything, return the original cycle
    return False, cycle

def main(N=6):

    #cyclic_sets = brute_force(N)
    cyclic_sets = DFS(N)
    print(cyclic_sets)

    total = sum(cyclic_sets[0])
    print(f"The sum of the only ordered set of {N} cyclic 4-digit numbers for which each polygonal type is represented by a different number in the set is:", total)
    return total

if __name__ == "__main__":
    main()