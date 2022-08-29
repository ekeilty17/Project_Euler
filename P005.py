from collections import Counter
import math

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


# The main idea is to just take all the common prime factors between every number in the interval
def minimum_divisible_by_interval(a, b):
    
    prime_factors = {}
    for n in reversed(range(a, b+1)):
        factors = Prime_Factors(n)
        C = Counter(factors)
        for p, freq in C.items():
            if p in prime_factors:
                prime_factors[p] = max(prime_factors[p], freq)
            else:
                prime_factors[p] = freq
    
    ans = 1
    for p, freq in prime_factors.items():
        ans *= p**freq
    
    return ans

def main(N=20):

    n = minimum_divisible_by_interval(1, N)
    
    print(f"The smallest positive number that is evenly divided by all numbers from 1 to {N}:", n)
    return n

if __name__ == "__main__":
    main(20)