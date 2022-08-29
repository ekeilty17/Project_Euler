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

def numberify(digits):
    return int( "".join([str(d) for d in digits]) )

def indices_of_same_elements(L):
    value_to_index = defaultdict(list)
    for i, x in enumerate(L):
        value_to_index[x].append(i)
    return value_to_index

def brute_force(N):

    sequences = []
    primes_checked = {}
    OoM = 1                                 # order of magnitude
    while len(sequences) == 0:

        prime_list = Sieve_of_Eratosthenes(10**OoM)
        primes_checked.update( {p : False for p in prime_list if p > 10**(OoM-1)} )
        
        for p in prime_list:
            # we don't need to check these again
            if p < 10**(OoM - 1):
                continue
            
            # skipping primes that have been checked in previous iterations
            if primes_checked[p]:
                continue

            # we get the location of all repeating digits in p
            digits = getDigits(p)
            digit_to_index = indices_of_same_elements(digits)
            
            # loop through every repeated digit index
            for d in digit_to_index:
                seq = []

                # and see if we get primes replacing them with all digits from 0-9
                for n in range(10):
                    q = numberify([n if i in digit_to_index[d] else x for i, x in enumerate(digits)])
                    if q in primes_checked:
                        primes_checked[q] = True
                        seq.append(q)

                # This does not count as a valid sequence: [07, 17, 37, 47, 67, 97]
                # i.e. the 7 should not be included
                # Therefore, we need to filter out anything from the sequence that used a leading 0
                seq = list(filter(lambda x: x > 10**(OoM-1), seq))
                
                # now, we only care about sequences of a certain length
                if len(seq) >= N:
                    #sequences.append(seq)
                    return seq              # if we only care about the smallest, we can just stop here
        
        # if we didn't find anything, increase the number of digits in the primes by 1
        OoM += 1

    return sequences[0]

def main(N=8):
    smallest_prime_family = brute_force(N)
    p = min(smallest_prime_family)

    print(f"The smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an {N}-prime value family is:", p)
    return p

if __name__ == "__main__":
    main()