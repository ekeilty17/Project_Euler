# integer factorization by Trial Division
def Prime_Factors(n):
    # Error Check
    if type(n) != int and type(n) != long:
        raise TypeError('must be integer')
    if n < 2:
        return []
    factors = []
    # as always, take care of the 2s first bc they are easy
    while n % 2 == 0:
        factors += [2]
        n =  n // 2
    # if n was purely a power of 2, then the function ends here
    if n == 1:
        return factors
    # since we got rid of the 2's potential factors, f can start at 3
    # other than that, this loop is pretty self explainitory
    f = 3
    while f*f <= n:
        if n % f == 0:
            factors += [f]
            n = n // f
        else:
            f += 2
    return factors + [n]

# See P069.py for explaination
def ProductFormula(n):
    if n < 1:
        return 0
    if n == 1:
        return 1
    f = list(set(Prime_Factors(n)))
    phi = n
    for p in f:
        phi -= (phi // p)       # The same as phi *= (1 - 1/p)
    return phi

def isPermutation(n, m):
    return list(sorted(str(n))) == list(sorted(str(m)))

# This produces the correct answer but is slow
def brute_force(N):
    permutations = []
    for n in range(2, N):
        phi_n = ProductFormula(n)
        if isPermutation(n, phi_n):
            permutations.append( (n, phi_n) )
    
    #print(permutations)
    minimum_permutation = min(permutations, key=lambda t: t[0]/t[1])
    return minimum_permutation

# TODO: come up with a better method
# I genuinly don't know how to improve it at this time though
# I'm thinking we can do something like the Sieve of Eratosthenes where producing all the phi's in a range
# is faster than producing them individually

def main(N=10**7):
    minimum_n, minimum_phi = brute_force(N)
    minimum_ratio = minimum_n / minimum_phi
    
    #print(minimum_n, minimum_phi, minimum_ratio)
    print(f"The value of 1 < n < {N}, for which phi(n) is a permutation of n and the ratio n / phi(n) produces a minimum is:", minimum_n)
    return minimum_n

if __name__ == "__main__":
    main()
