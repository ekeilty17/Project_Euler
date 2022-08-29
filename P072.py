from itertools import combinations
from functools import reduce

def gcd(a, b):
    if b > a:
        return gcd(b, a)
    if b == 0:
        return 0
    if a % b == 0:
        return b
    return gcd(b, a%b)

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


# There are two methods we could use to brute force it, 
# but it's just too many numbers to iterate over
def brute_force(N):
    #proper_fractions = []
    unique_fractions = set([])
    for d in range(2, N+1):
        for n in range(1, d):
            #if gcd(n, d) == 1:
            #    proper_fractions.append( (n, d) )
            unique_fractions.add( n/d )
    
    #return len(proper_fractions)
    return len(unique_fractions)


# There's a really nice way to generate all proper fractions
#                         1/2
#                  /              \
#            1/3                      2/3
#         /       \                /       \
#     1/4           3/4         2/5          3/5
#    /   \         /   \       /   \        /   \
#  1/5   4/5     3/7   4/7   2/7   5/7    3/8   5/8
#
# In general, if the node is a/b, to get the children we have
#       a/b     -->     a/(a+b)     and     b/(a+b)
# 
# And this will hit every proper fraction in reduce form
# We can also notice that the denominators monotonically increase, 
# so we can just prune nodes once the denominators are larger than N
#
# Unfortunately, this still takes too long
def tree_method(N):
    row = [(1, 2)]
    total = 1

    while len(row) > 0:
        next_row = []
        for a, b in row:
            d = a+b
            if d <= N:
                next_row.append( (a, d) )
                next_row.append( (b, d) )
        
        row = next_row
        total += len(row)
    
    return total


# So what we have learned is that any method of generating every fraction will take too long
# because the tree method is as efficient as you can be
# So instead, we need to have a clever method of counting the number of reduced proper fractions per denominator
#
# We notice that for each denominator d, the maximum number of possible reduced proper fractions is d-1 (numerators of 1 to d-1)
# 
# Now, we need to determine how many of these fractions are not in lowest terms
# This we can determined from the prime fractors of the denominator d
# i.e. each numberator that shares a prime factor with d will (by definition) be able to be reduced
# for each prime factor p, we will have (d/p)-1 reduceable fractions that we remove
#
# The tricky part is you can double count the removed fractions, 
#   for example, let d = 12
#   we would double count subtracting 6/12 because both primes 2 and 3 would remove it
# 
# To solve this, we have to keep track of when things are double counted
# we can do this by finding all the factors of d (not just the prime factors)
# Take 60 = 2*2*3*5 as an example:
#   if 0 < n < 60 is only a multiple of 2, 3, or 5 then it will be correctly counted
#   if 0 < n < 60 is only a multiple of 6, 10, or 15 then it will be double counted
#   if 0 < n < 60 is only a multiple of 30 then it will be triple counted
#
# We can notice that the number of times that n is redundantly counted is equal to the number of unique primes in the corresponding factor
# Therefore, we create the list [(2, 3, 5), (6, 10, 15), (30)]
# and update according to:
#       total += (-1)**(index+1)*(denominator/p-1)
def allFactors(prime_factors):
    factors = [prime_factors]
    for i in range(2, len(prime_factors)+1):
        temp = list(combinations(prime_factors, i))
        # a fancy way of multiplying everything in the tuples together
        factors += [tuple([reduce(lambda x, y: x*y, t) for t in temp])]

    return factors

def counting_using_factors(N):
    total = 0
    for d in range(2, N+1):
        
        total_with_denominator_d = d-1
        prime_factors = list(set(Prime_Factors(d)))
        factors_by_index = allFactors(prime_factors)
        mult = -1
        for F in factors_by_index:
            for f in F:
                if f > d:
                    continue
                total_with_denominator_d += mult * (d//f - 1)
            mult *= -1
        
        total += total_with_denominator_d
    
    return total


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

# We can use the same idea as the above method, 
# but we can use Euler's Totient function to count the number of elements that are relatively prime with d
# Which means my previous method is another way to calculate Euler's Totient function
def counting_using_totient_function(N):
    total = 0
    for d in range(2, N+1):
        
        phi_d = ProductFormula(d)
        total_with_denominator_d = phi_d
        total += total_with_denominator_d
    
    return total

def main(N=10**6):

    #total = brute_force(N)
    #total = tree_method(N)
    #total = counting_using_factors(N)
    total = counting_using_totient_function(N)

    print(f"The number of reduced proper fractions for d <= {N} is:", total)
    return total


if __name__ == "__main__":
    main()