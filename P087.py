import math

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


def brute_force(N):
    # we have N >= p^2 + q^3 < r^4 > p^2
    # so we need primes at least up until p = sqrt(N)
    upper_bound = math.ceil(math.sqrt(N))
    p = Sieve_of_Eratosthenes(upper_bound)

    j = 0
    k = 0
    nums = set([])
    for i in range(len(p)):
        x = p[i]**2 + p[j]**3 + p[k]**4
        while x < N:
            while x < N:
                #print(p[i], p[j], p[k])
                if x not in nums:
                    nums.add(x)
                k += 1
                x = p[i]**2 + p[j]**3 + p[k]**4
            j += 1
            k = 0
            x = p[i]**2 + p[j]**3 + p[k]**4
        j = 0
        k = 0
    
    return len(nums)

def main(N=5*10**7):
    total = brute_force(N)
    print(f"The number of natural numbers below {N} that can be expressed as the sum of a prime square, cube, and fourth power is:", total)
    return total

if __name__ == "__main__":
    main()