import math

def isPrime(n):
    # This helps rule out easy ones
    prime_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
                  43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

    if n < 2:
        return False
    if n in prime_list:
        return True
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

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


# Pollard's Rho Method
def Rho_Prime_Factors(n):
    # Error Checking
    if type(n) != int and type(n) != long:
        raise TypeError('must be integer')

    # finding the Greatest Common Divisor
    # This is the Euclidean Algorithm
    #   It takes adtantage of 3 facts
    #       1) any number can be written in this form a = qb + r
    #       2) gcd(a,b) = gcd(b,r)
    #       3) gcd(n,0) = n
    #   once r = 0 we have found the gcd of a and b
    def gcd(a,b):
        while b:
            a, b = b, a%b
        return abs(a)

    #this function just finds 1 prime factor
    def rho_factor(n, c):
        f = lambda x: (x*x+c) % n # creating a prototype of x^2+c (mod n)
        t = 2 # tortoise
        h = 2 # hair
        d = 1
        # here's the clever part of the algorithm, 
        # Floyd's method for detecting cycles works in tandum with finding p
        # since t and h both start at 2, f(f(h)) is the same as f(f(t)), 
        # and f(x) = x in the next iteration
        # this means gcd(t-h, n) is the same as gcd(x-f(x), n)
        while d == 1:
            t = f(t)        # tortoise goes 1 step
            h = f(f(h))     # while the hare goes 2 steps
            d = gcd(t-h,n)
        if d == n: # the factor gave no new information, so try another c value
            return rho_factor(n, c+1)
        if isPrime(d): # if the factor is a prime, then yay we did it
            return d
        return rho_factor(d, c+1)

    if -1 <= n <= 1: # account for degenerate cases
        return [n]
    if n < -1: # cute way to account for negatives
        return [-1] + rho_factors(-n)
    prime_factors = []
    while n % 2 == 0: # get rid of the other degenerate case
        n = n // 2
        prime_factors += [2]
    if n == 1:
        return prime_factors
    while not isPrime(n):
        f = rho_factor(n, 1)
        n = n // f
        prime_factors += [f]
    return sorted(prime_factors + [n])

def main(N=600851475143):

    prime_factors = Prime_Factors(N)
    #prime_factors = Rho_Prime_Factors(N)
    max_factor = max(prime_factors)

    print(f"The prime factorization of {N}:", prime_factors)
    print(f"The largest prime factor of {N}:", max_factor)
    return max_factor

if __name__ == "__main__":
    main()