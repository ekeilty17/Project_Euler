def get_factors(n):
    result = set([])
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            result.add(i)
            result.add(n//i)
    return result

def get_factor_chain(n, factor_sum):
    if n == 0:
        return []

    chain = []
    limit = len(factor_sum)-1

    curr, nxt = n, factor_sum[n]
    while curr not in chain:
        chain.append(curr)
        if nxt > limit:
            return []
        curr, nxt = nxt, factor_sum[nxt]
    
    return chain

# This works, it's not super slow because we preprocess a lot of the computation in the `factor_sum` list
def brute_force(N):

    # we pre-process all the factor sums
    factor_sum = [None]*(N+1)
    factor_sum[0] = 0               # include these to help indexing
    factor_sum[1] = 1

    for n in range(2, N+1):
        f = get_factors(n)
        factor_sum[n] = (sum(f) - n)     # the factor set includes the number itself
    

    # then, we just need to search for the longest chain
    chains = [get_factor_chain(n, factor_sum) for n in range(N+1)]

    # finding amicable chains
    amicable_chains = []
    for n in range(N+1):
        if chains[n] == []:
            continue
        if factor_sum[ chains[n][-1] ] == n:
            amicable_chains.append( chains[n] )
    
    longest_chain = max(amicable_chains, key=len)
    return longest_chain


# calculating all factors of every number from 1 to N
# uses a Sieve of Eratosthenes like approach
def get_all_factors_to_limit(N):
    factors = [[1, n] for n in range(N+1)]
    factors[0] = []
    factors[1] = [1]
    for n in range(2, N+1):
        for k in range(2, N//n+1):
            factors[k*n].append(n)
    return factors


# we make two improvements based on computing the group 1 to N in tandem as opposed to independently
#   1) computing factors
#   2) computing chains
# This is reasonably fast, and I don't see a way to improve it
def brute_force_more_efficient(N):

    # we pre-process all the factor sums
    # TODO: This is still the slowest part, but I don't see how you make it any faster
    factors = get_all_factors_to_limit(N)
    factor_sum = [sum(factors[n]) - n for n in range(N+1)]
    factor_sum[0] = 0               # include these to help indexing
    factor_sum[1] = 1

    # then, we just need to search for the longest chain
    chains = [[] for n in range(N+1)]
    chains[0] = [0]                 # include these to help indexing
    chains[1] = [1]

    # computing chains
    # This is now quite quick
    for n in range(2, N+1):
        curr, nxt = n, factor_sum[n]
        while curr not in chains[n]:
            chains[n].append(curr)
            
            # reach limit
            if nxt > N:
                chains[n] = []
                break
            
            # if we already calculated nxt, then we can use the previous computation
            if chains[nxt] != []:
                i = len(chains[nxt])
                if n in chains[nxt]:
                    i = chains[nxt].index(n)
                elif curr in chains[nxt]:
                    i = chains[nxt].index(curr)
                chains[n].extend( chains[nxt][:i] )
                break
            curr, nxt = nxt, factor_sum[nxt]

    # finding amicable chains
    # same as previous
    amicable_chains = []
    for n in range(2, N+1):
        if len(chains[n]) == 0:
            continue
        if factor_sum[ chains[n][-1] ] == n:
            amicable_chains.append( chains[n] )
    
    longest_chain = max(amicable_chains, key=len)
    return longest_chain


def main(N=10**6):
    #longest_chain = brute_force(N)
    longest_chain = brute_force_more_efficient(N)

    #print(longest_chain)
    min_element = min(longest_chain)
    print(f"The smallest member of the longest amicable chain with no element exceeding {N} is:", min_element)
    return min_element

if __name__ == "__main__":
    main()