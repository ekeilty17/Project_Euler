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

def isSquare(n):
    if n < 0:
        return False
    x = math.sqrt(n)
    return n == (math.floor(x))**2 or n == (math.ceil(x))**2

# The brute force method is pretty fast in this case
def brute_force(N):
    
    OoM_primes = 2
    prime_list = Sieve_of_Eratosthenes(10**OoM_primes)
    
    n = 5
    counter_examples = []
    while len(counter_examples) < N:
        for p in prime_list:
            if p > n:
                # we didn't find an example
                counter_examples.append(n)
                break
            if p == n:
                break
            m = n - p
            if m % 2 == 1:
                continue
            if isSquare(m//2):
                break
        else:
            # I got to the end of the for loop without breaking, which means I didn't have enough primes
            # so I increase my prime_list
            OoM_primes += 1
            prime_list = Sieve_of_Eratosthenes(10**OoM_primes)

            # this is so I repeat the previous check
            n -= 2
        
        n += 2
    
    return counter_examples


def main(N=1):
    counter_examples = brute_force(N)
    print(counter_examples)

    print(f"The smallest odd composite that cannot be written as the sum of a prime and twice a square is:", counter_examples[0])
    return counter_examples[0]

if __name__ == "__main__":
    main()