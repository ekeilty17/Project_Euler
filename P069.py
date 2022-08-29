import numpy as np

def gcd(a, b):
    if b > a:
        return gcd(b, a)
    if a % b == 0:
        return b
    return gcd(b, a%b)

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



# Very, very slow
def brute_force(n):
    if n < 1:
        return []
    if n == 1:
        return [1]
      
    relatively_prime = [1]
    for i in range(2, n):
        if gcd(n, i) == 1:
            relatively_prime.append(i)
    
    #print(relatively_prime)
    return len(relatively_prime)


# We use some properties of Euler's Totient function
#   If n is prime, phi(n) = n-1
#   If m and n are coprime, phi(n*m) = phi(n)*phi(m)
#   If a and n are coprime, a^phi(n) % n = 1
#
# You can go to the wikipedia page: https://en.wikipedia.org/wiki/Euler%27s_totient_function
# to see how we derive Euler's product formula
#   Let n = p1^a1 * p2^a2 * ... * pm^am
#   Then phi(n) = n * (1 - 1/p1) * (1 - 1/p2) * ... * (1 - 1/pm)
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


# From the above, let n = p1^a1 * p2^a2 * ... * pm^am
# Then phi(n) = n * (1 - 1/p1) * (1 - 1/p2) * ... * (1 - 1/pm)
#
# We wish to maximize n / phi(n) = 1 / [ (1 - 1/p1) * (1 - 1/p2) * ... * (1 - 1/pm) ]
# Therefore, we just want the number below N with the most number of distinct, small prime factors
def math_solution(N):
    prime_list = Sieve_of_Eratosthenes(N)

    i = 0
    n_max = 1
    while n_max * prime_list[i] < N:
        n_max *= prime_list[i]
        i += 1
    
    return n_max

def main(N=10**6):
    phi = []
    for n in range(N):
        #phi_n = brute_force(n)
        phi_n = ProductFormula(n)
        
        phi.append( phi_n )
        #print(n, phi_n)

    # calculating n / phi(n) for each ratio
    ratio = [0] + [n / phi[n] for n in range(2, N)]

    # getting the maximum
    ratio_max = max(ratio)
    n_max = np.argmax(ratio)

    #n_max = math_solution(N)
    #ratio_max = n_max / ProductFormula(n_max)

    #print(ratio_max)
    print(f"The value of n <= {N} for which the ratio n / phi(n) is maximum is:", n_max)
    return n_max

if __name__ == "__main__":
    main()