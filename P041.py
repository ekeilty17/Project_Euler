import itertools

def isPrime(n):
    if n <= 0:
        return False
    if n == 1:
        return False
    prime_list = [  2,   3,   5,   7,   11,  13,  17,  19,  23,  29,  31,  37,  41,  43,  47,
                    3,   59,  61,  67,  71,  73,  79,  83,  89,  97,  101, 103, 107, 109, 113,
                    127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]
    if n in prime_list:
        return True
    for i in range(2,int(n**(0.5))+1):
        if n % i == 0:
            return False
    return True

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

def isPandigital(n):
    digits = getDigits(n)
    return list(sorted(digits)) == list(range(1, len(digits)+1))

""" Observation: 
        we can actually eliminate any pandigital number of length 8 or 9 
        because 1+2+3+4+5+6+7+8 and 1+2+3+4+5+6+7+8+9 will always be divisible by 3
        so we only have to search up to pandigital primes of length n=7
"""

# This starts with all primes, and then filters out the ones that are pandigital
# it's pretty quick, espeically after eliminating primes of length 8 or 9
def pandigital_elimination():
    prime_list = Sieve_of_Eratosthenes(10**7)
    pandigital_prime_list = list(filter(lambda p: isPandigital(p), prime_list))
    return max(pandigital_prime_list)

# This finds all pandigital numbers, and then filters out the primes
# This turns out to be faster because we can eliminate so many pandigital number lengths
def prime_elimination():
    # 1+2, 1+2+3, 1+2+3+4+5, 1+2+3+4+5+6, 1+2+3+4+5+6+7+8, and 1+2+3+4+5+6+7+8+9 are all divisible by 3
    pandigital_prime_list = []
    for n in [4, 7]:
        for perm in itertools.permutations(list(range(1, n+1))):
            p = int("".join([str(d) for d in perm]))
            if isPrime(p):
                pandigital_prime_list.append(p)
    return max(pandigital_prime_list)

def main(N=9):

    #largest_pandigital_prime = pandigital_elimination()
    largest_pandigital_prime = prime_elimination()
    print(f"The largest prime with consecutive digits 1 to n for some n is:", largest_pandigital_prime)
    return largest_pandigital_prime

if __name__ == "__main__":
    main()