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

def decimal_expansion(a, b, num_digits=10):
    ans = [a//b, '.']
    a = 10*(a%b)
    for _ in range(num_digits):
        ans += [a//b]
        a = 10*(a%b)
    return ans

# This works if num_digits < 18, but we need a lot more digits than that, hense the above function
def decimal_expansion2(a, b, num_digits=10):
    return str(a/b)[:num_digits+2]

def get_cycle_length(a, b, num_digits=20):
    digits = decimal_expansion(a, b, num_digits)
    
    # first digits don't matter
    digits = digits[2:]

    # removing lead zeros
    k = 0
    while True:
        if digits[k] != 0:
            break
        k += 1
    digits = digits[k:]

    # finding cycle
    for l in range(4, len(digits)):                         # length of the cycle
        for i in reversed(range(l, len(digits)-l+1, l)):    # index into the digits
            if digits[i-l:i] == digits[i:i+l]:
                return l
        
    return -1

def main(N=1000):
    # we only have to consider primes as cycles of any composite number is just the maximum of the cycles of its prime factors
    prime_list = Sieve_of_Eratosthenes(N)

    max_cycle = 0
    num = 0
    for p in prime_list:
        c = get_cycle_length(1, p, 10*N)     # I can't prove it, but I feel like a cycle can't be longer than 10 * the number 
        if c > max_cycle:
            max_cycle = c
            num = p
    
    print(f"the value of d < {N} for which 1/d contains the longest recurring cycle in its decimal fraction part is:", num)
    return num

if __name__ == "__main__":
    main()