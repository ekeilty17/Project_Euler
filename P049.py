from collections import defaultdict
from itertools import chain, combinations

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

def getDigits(n):
    return [int(d) for d in str(n)]

def powerset(L, include_self=True):
    n = len(L)
    if include_self:
        n += 1
    return chain.from_iterable(combinations(L, r) for r in range(n))

def isArithmeticSequence(*args):
    if len(args) < 2:
        return True
    
    # I am assuming that args is in the correct order
    diff = args[1] - args[0]
    for i in range(len(args)-1):
        if args[i+1] - args[i] != diff:
            return False
    return True

def arithmetic_sequences(d, length):
    
    prime_list = Sieve_of_Eratosthenes(10**d)
    prime_list = list(filter(lambda p: len(str(p)) == d, prime_list))

    # all primes with N-digits that are permutations of each other
    Permutations = defaultdict(list)
    for p in prime_list:
        Permutations[tuple(sorted(getDigits(p)))].append( p )

    sequences = []
    for key in Permutations.keys():
        seq = list(sorted(Permutations[key]))
        if len(seq) >= length:
            # there could be other permutations that are primes that don't produce an arithmetic sequence
            # so we need to check all powersets
            for subseq in powerset(seq):
                # by checking the length first, we prune a lot of subsequences very quickly
                if len(subseq) >= length and isArithmeticSequence(*subseq):
                    sequences.append(subseq)
    
    return sequences

def main(d=4, length=3):
    sequences = arithmetic_sequences(d, length)
    seq = sequences[-1]

    print(f"All {d}-digit increasing arithmetic sequence of length {length}:", sequences)
    return seq

if __name__ == "__main__":
    main()