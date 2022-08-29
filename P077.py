import numpy as np

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

# This is basically the same as problem 31 where we just have that the "coin" set is the prime set
# So see P031.py for an explanation of the dynamic programming solution
def P_prime(n):    

    prime_list = Sieve_of_Eratosthenes(n)
    partitions = [0] * (n+1)
    partitions[0] = 1
    
    for p in prime_list:
        for j in range(p, n+1):
            partitions[j] += partitions[j - p]

    return partitions[n]


# Using this will give the same result as above, it's just a less elegant way of doing it
# but, this form of the above method allows us to replace the first for-loop with a while loop
# in order to increment n until we find one such that p_prime(n) > N
def P_prime_less_elegant(n):
    
    prime_list = Sieve_of_Eratosthenes(n)
    partitions = np.zeros((n+1, len(prime_list)), dtype=int)
    partitions[0, :] = 1                # base-case: number of ways to make a total of 0 is 1...do nothing

    for j in range(1, n+1):
        for i in range(len(prime_list)):
            p = prime_list[i]
            partitions[j, i] = partitions[j, i-1]
            if j >= p:
                partitions[j, i] += partitions[j-p, i]
    
    return partitions[n, -1]


def search(N):
    prime_list = Sieve_of_Eratosthenes(N)
    partitions = np.zeros((N+1, len(prime_list)), dtype=int)
    partitions[0, :] = 1                # base-case: number of ways to make a total of 0 is 1...do nothing
    
    n = 0
    while partitions[n, -1] < N:
        n += 1
        for i in range(len(prime_list)):
            p = prime_list[i]
            partitions[n, i] = partitions[n, i-1]
            if n >= p:
                partitions[n, i] += partitions[n-p, i]
    
    #print(partitions[n, -1])
    return n


def main(N=5000):
    
    """
    n = 2
    num_prime_partitions = P_prime(n)
    while num_prime_partitions <= N:
        n += 1
        num_prime_partitions = P_prime(n)
    """

    n = search(N)
    print(f"The first number that can be written as the sum of primes in over {N} different ways is:", n)
    return n

if __name__ == "__main__":
    main()