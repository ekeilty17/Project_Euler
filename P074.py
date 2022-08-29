from collections import defaultdict


def getDigits(n):
    return [int(d) for d in str(n)]

def sortedDigits(n):
    return tuple(sorted(getDigits(n)))

# This gives the factorial of any number between [0, 9] inclusive
def factorial(n):
    F = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
    return F[n]

def DigitFactorial(n):
    return sum(map(factorial, getDigits(n)))

def Chain(n):
    d = DigitFactorial(n)
    chain = [n]
    while d not in chain:
        chain.append(d)
        d = DigitFactorial(d)
    return chain

def ChainLength(n):
    d = DigitFactorial(n)
    chain = set([n])
    while d not in chain:
        chain.add(d)
        d = DigitFactorial(d)
    return len(chain)

# Obviously this is slow
def brute_force_naive(N, r):

    r_length_chains = []
    for n in range(N):
        chain_length = ChainLength(n)
        if chain_length == r:
            r_length_chains.append(chain_length)
        
        #print(n, chain_length)

    return len(r_length_chains)


# by noticing the order of the digits doesn't matter when calculating the digit factorial
# we can remember past solutions to greatly reduce the computation
# This is actually pretty fast
def brute_force_memoization(N, r):

    chain_lengths = defaultdict(int)        # defaults to a value of 0
    for n in range(N):
        n_digits = sortedDigits(n)

        if chain_lengths[n_digits] == 0:
            chain_lengths[n_digits] = ChainLength(n)
        
        #print(n, chain_lengths[n_digits])

    r_length_chains = [n for n in range(N) if chain_lengths[sortedDigits(n)] == r]
    return len(r_length_chains)


# TODO: ran into some issues with this that I didn't feel like fixing
"""
# we can do even better by also applying memoization when calculating the chain
# so if we ever enounter a number on the chain that we've seen before, we can stop and figure out the new chain length
# Suppose we have chain
#                   a1 --> a2 --> a3 --> ... --> an --> c1 --> c2 --> ... --> cm --> c1
#
# The chain lengths for each element is given by the folllowing
#       chain_length[a1] = n + m
#       chain_length[a_{i+1}] = chain_length[ai] - 1
#       chain_length[ci] = m
def brute_force_memoization2(N, r):

    chain_lengths = defaultdict(int)
    for n in range(N):
        n_digits = sortedDigits(n)

        # all the things we need to keep track of
        d = n
        d_digits = sortedDigits(d)
        repeated_index = None
        
        chain = []
        while chain_lengths[d_digits] == 0:
            if d in chain:
                repeated_index = chain.index(d)
                chain_lengths[n_digits] = len(chain)
                print(d, repeated_index, )
                break
            
            chain.append(d)
            d = DigitFactorial(d)
            d_digits = sortedDigits(d)
        
        for i in range(len(chain)):
            if i <= repeated_index:
                chain_lengths[sortedDigits(chain[i+1])] = chain_lengths[sortedDigits(chain[i])]-1
            else:
                chain_lengths[sortedDigits(chain[i])] = len(chain) - repeated_index
        
        print(n, chain_lengths[n_digits])
    
    r_length_chains = [n for n in range(N) if chain_lengths[sortedDigits(n)] == r]
    return len(r_length_chains)
"""

def main(N=10**6, r=60):

    #total = brute_force_naive(N, r)
    total = brute_force_memoization(N, r)
    print(f"The number of chains starting with a number below {N} that contains exactly {r} non-repeating terms is:", total)
    return total

if __name__ == "__main__":
    main()