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

def isAbundant(n):
    if sum(factors(n)) > n:
        return True
    return False

def main():
    upper_bound = 28123
    abundant = [n for n in range(0, upper_bound+1) if isAbundant(n)]

    abundant_sums = [False] * (upper_bound + 1)
    
    for i in range(len(abundant)):
        a = abundant[i]
        for j in range(i, len(abundant)):
            b = abundant[j]
            if a + b > upper_bound:
                break
            abundant_sums[a + b] = True

    total = sum([i for i in range(len(abundant_sums)) if not abundant_sums[i]])
    print(f"The sum of all the positive integers which cannot be written as the sum of two abundant numbers:", total)
    return total

if __name__ == "__main__":
    main()