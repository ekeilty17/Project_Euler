from collections import Counter
import math

def square_digits(n):
    return sum([int(x)**2 for x in str(n)])

def getDigits(n):
    return [int(d) for d in str(n)]

def Chain(n):
    chain = [n]
    while n != 1 and n != 89:
        n = square_digits(n)
        chain.append(n)
    return chain

# very slow
def brute_force(N):

    total = 0
    for n in range(1, N):
        #print(n)
        if Chain(n)[-1] == 89:
            total += 1

    return total

# idea is to keep track of previous computations
def better_brute_force(N):

    chain_endpoints = [None] * N
    chain_endpoints[0] = 0          # just included for intuitive indexing
    chain_endpoints[1] = 1
    chain_endpoints[89] = 89

    for n in range(1, N):
        #print(n)

        chain = [n]
        while chain_endpoints[n] is None:
            n = square_digits(n)
            chain.append(n)
        
        endpoint = chain_endpoints[n]
        for x in chain:
            chain_endpoints[x] = endpoint

    return len([n for n in range(N) if chain_endpoints[n] == 89])

# This is about as fast a brute force can be
# we notice that when n is large, the square digit sum of their digits is much much smaller
# so we can upper bound it, do a straight forward search on these and store the results
# Then, for all numbers larger than this, we just have to compute 1 square digit sum
def even_better_brute_force(N):

    # no number with the same number of digits as N can have a square digit sum greater than 9^2 + 9^2 + ... + 9^2
    upper_bound = (9**2) * len(str(N))

    # we pre-compute where the chain ends for each of these numbers
    chain_endpoints = [False] * (upper_bound + 1)
    for n in range(1, upper_bound+1):
        chain = Chain(n)
        if chain[-1] == 89:
            chain_endpoints[n] = True
    
    # Then, we can iterate over each number from 1 to N, 
    # which now requires a constant about of computation to determine where the chain ends
    # Therefore, with a negligable amount of pre-computation, we can make the brute force algorithm O(N)
    total = 0
    for n in range(1, N):
        print(n)
        x = square_digits(n)
        if chain_endpoints[x]:
            total += 1
    
    return total


# The brute force method still isn't fast enough for my liking because N is very large
# We can do better by taking advantage of the fact that the order of the digits doesn't matter
# Therefore, we can iterate through the digits in sorted order, for example
#       00, 01, 02, 03, 04, 05, 06, 07, 08, 09
#           11, 12, 13, 14, 15, 16, 17, 18, 19
#               22, 23, 24, 25, 26, 27, 28, 29
#                   33, 34, 35, 36, 37, 38, 39
#       ... etc
#
# We know from before, we can just recompute the answer for a small set of numbers and use that for any number <N
# 
# Suppose we determine that n leads to an 89 (with n's digits being in sorted order)
# we need to count the number of permutations of the digits of n, so we can add the appropriate total
# if the digits of n are (d1, d2, ..., dm), then we use the multinomial coefficient formula
#       (permutations of digits of n) = n! / ( (# of digits that are 0)! * (# of digits that are 1)! * ... * (# of digits that are 9)! )
#
# The running time of this method is the number of iterations we need
# which is the number of numbers < N whose digits are in non-descreasing order
# This is a variant of the weakened stars and bars combinatorial problem, which says this answer is
#       10 + num_digits choose num_digits
# where num_digits = O(log(N))
def factorial_list(n):
    out = [1]
    f = 1
    for i in range(1, n+1):
        f *= i
        out += [f]
    return out

def counting(N):
    # Note that this assumes that N is a perfect power of 10
    num_digits = len(str(N)) - 1
    F = factorial_list(num_digits)

    # calculate upperbound just as before
    upper_bound = (9**2) * num_digits
    chain_endpoints = [False] * (upper_bound + 1)
    for n in range(1, upper_bound+1):
        chain = Chain(n)
        if chain[-1] == 89:
            chain_endpoints[n] = True
    
    total = 0

    # we use my N-forloop code to efficiently iterate over each permutation of digits in sorted order
    digits = [0] * num_digits
    i = 0
    while i < num_digits:
        # This is all the logic to iterate through the digits
        if digits[i] >= 9:
            digits[i] = 0
            i += 1
            continue
        digits[i] += 1
        for k in range(i+1):
            digits[k] = digits[i]       # this ensures that we iterate in sorted order (repeated digits allowed)
        i = 0
        
        # just as before, we get the chain endpoint
        x = sum([d**2 for d in digits])
        if chain_endpoints[x]:
            # now I need to calculate the number of permutations of this number
            C = Counter(digits)
            total += int(F[num_digits] / math.prod([F[cnt] for _, cnt in C.items()]) )      # total up the permutations

    return total
        

def main(N=10**7):

    #total = brute_force(N)
    #total = better_brute_force(N)
    #total = even_better_brute_force(N)
    total = counting(N)
    print(f"The number of numbers less than {N} whose square chains arrive at 89 is:", total)
    return total

if __name__ == "__main__":
    main()