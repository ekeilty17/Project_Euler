import math

def isPrime(n):
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

def brute_force(N):

    max_consecutive_primes = 0
    coef = None

    for a in range(-N, N+1):
        for b in range(-N, N+1):
            n = 0
            p = n**2 + a*n + b
            while isPrime(p):
                n += 1
                p = n**2 + a*n + b
            if n > max_consecutive_primes:
                max_consecutive_primes = n
                coef = (a, b)

    return coef

# TODO: make something more efficient

def main(N=1000):
    
    coef = brute_force(N)

    product = coef[0] * coef[1]
    print(f"The product of the coefficients for the maximum consecutive primes:", product)
    return product

if __name__ == "__main__":
    main()