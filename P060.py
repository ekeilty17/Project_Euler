import itertools

def isPrime(n):
    if n <= 0:
        return False
    if n == 1:
        return False
    prime_list = [  2,   3,   5,   7,   11,  13,  17,  19,  23,  29,  31,  37,  41,  43,  47,
                    3,   59,  61,  67,  71,  73,  79,  83,  89,  97,  101, 103, 107, 109, 113,
                    127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]
    if n in prime_list:
        return True
    for i in range(2, int(n**(0.5))+1):
        if n % i == 0:
            return False
    return True

def Sieve_of_Eratosthenes(n):
    #Error Check
    if type(n) != int and type(n) != long:
        raise TypeError("must be integer")
    if n < 2:
        raise ValueError("must be greater than one")
    m = (n-1) // 2 #list only needs to be half as long bc we dont care about even numbers
    sieve = [True] * m
    i = 0
    p = 3
    prime_list = [2] #add 2 as the exception
    #this while loop is equivilent to the while loop in the first Sieve function
    #it just looks different because the parameters are different
    while p*p < n:
        #if the number hasnt been crossed out we add it
        if sieve[i]:
            prime_list += [p]
            #j is the multiples of p
            j = 2*i*i + 6*i + 3 #j = (p^2-3)/2 where p = 2i+3 (see below comments)
            #this is equivilent to the for loop in the previous Sieve fuction
            while j < m:
                sieve[j] = False
                j += 2*i + 3 #p = 2i+3
        i += 1
        p += 2
        #this is where the p = 2i+3
        #p starts at 3 and is upped by 3, where i starts at 0 and is upped by 1
    #this while loop then adds the remaining primes to the prime list
    while i < m:
        if sieve[i]:
            prime_list += [p]
        i += 1
        p += 2
    return prime_list


def concat(a, b):
    return int(str(a) + str(b))

def isPairwiseConcatenatingPrimes(p, q):
    return isPrime(concat(p, q)) and isPrime(concat(q, p))

def find_pairs(p, prime_list):
    p_pairs = set([])
    for q in prime_list:
        if isPairwiseConcatenatingPrimes(p, q):
            p_pairs.add(q)
    return p_pairs


def brute_force(N):
    prime_list = Sieve_of_Eratosthenes(30000)           # we choose 30,000 because the algorithm will show that 
                                                        # 26,033 is the minimum sum, we so we can know no other smallest sum exists
    
    smallest_sum_set = tuple( [prime_list[-1]] * N )
    smallest_sum = sum(smallest_sum_set)
    pairs = [None] * len(prime_list)

    i = 0
    candidate_set = []
    indices = []
    while True:
        # successfully found concatenating pairwise prime set
        if len(candidate_set) == N:
            if sum(candidate_set) < sum(smallest_sum_set):
                smallest_sum_set = list(sorted(candidate_set))
                smallest_sum = sum(smallest_sum_set)
                indices = indices[:-1]
                candidate_set = candidate_set[:-1]
        
        # base-case, we ran out of primes
        if i >= len(prime_list):
            if len(candidate_set) == 0:
                # we failed to find a set of size N
                break
            
            i = indices[-1] + 1
            indices = indices[:-1]
            candidate_set = candidate_set[:-1]
            # we need to continue so we check i again
            continue

        #print(*candidate_set, prime_list[i])

        # pruning steps
        #   since we are iterating in numerical order
        #   if adding the next smallest primes results in a larger sum, we can stop searching
        diff = N - len(candidate_set)
        if sum(candidate_set) + prime_list[i] * diff > smallest_sum:
            if len(candidate_set) == 0:
                break
            else:
                i = indices[-1] + 1
                indices = indices[:-1]
                candidate_set = candidate_set[:-1]
                continue
        
        p = prime_list[i]
        for j, q in zip(indices, candidate_set):
            if not (p in pairs[j]):
                break
        else:
            # only executes if we don't break, i.e. we can add p to the candidate set
            #   Now we calculate all possible pairwise concatenating primes and store it so we don't have to do it again later
            if pairs[i] is None:
                pairs[i] = find_pairs(prime_list[i], prime_list[i+1:])
            # if there aren't enough pairs, then we don't have to look any farther
            if len(pairs[i]) >= diff:
                candidate_set.append(p)
                indices.append(i)
        
        i += 1

    return tuple(sorted(smallest_sum_set))


# This is a bit slow, but it gives the correct answer. And I think it's just because I've coded this is python instead of C
# it's instantaneous for N<5, but takes about a 2 minutes for N=5
# this is an improvement over the brute force, which I have never seen finish for N=5
# so I am going to take it
def constructive(N):

    OoM = 1
    prime_list = Sieve_of_Eratosthenes(10**OoM)
    prime_set = [tuple([p]) for p in prime_list]

    # we iteratively build up the solution
    n = 2
    while n < N+1:
        n_wise = set([])
        
        # we take two prime sets of length n-1 and if they contain n-2 elements in common, we can construct a new list of size n
        for P, Q in itertools.combinations(prime_set, 2):
            # pruning combinations
            A, B = set(P), set(Q)
            if len(A.intersection(B)) != n-2:
                continue
            
            # if the two that are not in common pair-wise concatenating prime, then the union of the set are also
            p = (A - B).pop()
            q = (B - A).pop()
            if isPairwiseConcatenatingPrimes(p, q):
                n_wise.add( tuple(sorted(A.union(B))) )
        
        if len(n_wise) == 0:
            # we keep increasing the number of primes we consider until we get the answer
            OoM += 1
            prime_list = Sieve_of_Eratosthenes(10**OoM)
            prime_set = [tuple([p]) for p in prime_list]
            n = 2
        else:
            # otherwise we continue and iterate forward
            prime_set = n_wise
            n += 1

    return min(prime_set, key=lambda S: sum(S))


def main(N=5):

    #minimum_pairwise_concatenating_primes = brute_force(N)
    minimum_pairwise_concatenating_primes = constructive(N)
    print(minimum_pairwise_concatenating_primes)

    print(f"The lowest sum for a set of {N} primes for which any two primes concatenate to produce another prime is:", sum(minimum_pairwise_concatenating_primes))
    return sum(minimum_pairwise_concatenating_primes)

if __name__ == "__main__":
    main()