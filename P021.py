from itertools import chain, combinations
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

def powerset(L, include_self=True):
    n = len(L)
    if include_self:
        n += 1
    return chain.from_iterable(combinations(L, r) for r in range(n))

def factors(n):
    prime_factors = Prime_Factors(n)
    f = set()
    for subset in powerset(prime_factors, include_self=False):
        f.add(math.prod(subset))
    return f

def d(n):
    f = factors(n)
    return sum(f)

def isAmicable(a):
    b = d(a)
    if a == b:
        return False
    if a == d(b):
        return True
    else:
        return False

def main(N=10000):
    amicable = []
    for i in range(1, N+1):
        if isAmicable(i):
            amicable += [i]

    total = sum(amicable)
    print(f"The sum of all the amicable numbers under {N} is:", total)
    return total

if __name__ == "__main__":
    main()
