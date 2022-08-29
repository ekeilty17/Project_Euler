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

def numDigits(n):
    return len(str(n))

def rotate(n):
    one = n%10
    d = numDigits(n)
    n = n // 10
    n += one*(10**(d-1))
    return n

# This will determine if a specific n is circular
def isCircular(n):
    d = numDigits(n)
    for i in range(0, d):
        if not isPrime(n):
            return False
        n = rotate(n)
    return True

# and the brute force algorithm is very straight forward, but very redundant because 
# we will check say 197, 971, and 719 all individually when we only need to check one of them
def brute_force(N):
    circular_primes = []
    for p in prime_list:
        if isCircular(p):
            circular_primes.append(p)
    
    return list(sorted(set(circular_primes)))


# but it's more efficient to check for all circular primes less than N
def get_circular_primes(N):
    # The key idea is to do a bunch of pre-processing so that checking for circular primes is fast
    # we compute all primes under N (i.e. all candidates) and then we have a list to keep track of ones we've already checked
    prime_list = Sieve_of_Eratosthenes(N)
    prime_to_index = {p: i for i, p in enumerate(prime_list)}
    primes_checked = [False] * len(prime_list)

    # Since we have this index list, the order in which we check the primes doesn't matter
    # so we can make our prime list into a set, to make look-up constant time
    prime_list = set(prime_list)

    circular_primes = []
    for p in prime_list:
        # skip if we've already checked it
        if primes_checked[prime_to_index[p]]:
            continue
        
        # check for circular condition
        primes = []
        for _ in range(numDigits(p)):
            if p in prime_list:
                j = prime_to_index[p]
                primes.append(p)
                primes_checked[j] = True
            else:
                # This means p is not in prime_list, therefore we break because not all the rotated numbers are prime
                break
            p = rotate(p)
        else:
            # this only executes if we didn't break out of the for loop, i.e. all rotations were prime
            circular_primes.extend(primes)

    # even though it looks like 2 nested for loops, because of the primes_checked list, we only every process each prime twice
    # Therefore, the above is just O(N)
    return list(sorted(set(circular_primes)))

def main(N=10**6):

    #circular_primes = brute_force(N)
    circular_primes = get_circular_primes(N)

    print(f"The number of circular primes below {N} is:", len(circular_primes))
    return len(circular_primes)

if __name__ == "__main__":
    main()