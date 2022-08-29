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
    for i in range(2, int(n**(0.5))+1):
        if n % i == 0:
            return False
    return True

# The brute force is pretty fast, there are probably some more optimizations
def brute_force(N):
    prime_list = Sieve_of_Eratosthenes(N)

    longest_seq = []
    for i in range(len(prime_list)):
        for j in range(i+1, len(prime_list)):
            subseq = prime_list[i:j]
            p = sum(subseq)
            if p > N:
                break
            if isPrime(p):
                if len(subseq) > len(longest_seq):
                    longest_seq = subseq
        
        # some more pruning, if we don't have enough primes left after i to break our longest sequence
        # then we don't have to check them
        if len(prime_list) - i < len(longest_seq):
            break
    
    return longest_seq
            

def main(N=10**6):

    seq = brute_force(N)
    p = sum(seq)
    #print(seq)
    print(f"The largest prime under {N} that can be written as the sum of the most consecutive primes is:", p)
    return p

if __name__ == "__main__":
    main()