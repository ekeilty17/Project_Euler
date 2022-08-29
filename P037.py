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

def numDigits(n):
    return len(str(n))

def rm_left(n):
    return n % (10**(numDigits(n)-1))

def rm_right(n):
    return n//10

def isTruncatable_left(p):
    while p != 0:
        if not isPrime(p):
            return False
        p = rm_left(p)
    return True

def isTruncatable_right(p):
    while p != 0:
        if not isPrime(p):
            return False
        p = rm_right(p)
    return True


# The brute force approach actually isn't that bad, mostly because in the isPrime function we have the first 200 primes stored
def brute_force():
    dual_truncatable_primes = []
    p = 10
    while len(dual_truncatable_primes) < 11:            # the problem tells us that there are exactly 11 such primes
        if isTruncatable_left(p) and isTruncatable_right(p):
            #print(p)
            dual_truncatable_primes.append(p)

        p += 1
    
    return dual_truncatable_primes


# But theoretically, this is a much better algorithm
def dynamic_programming():
    #                       0       1     2     3      4     5      6      7     8      9
    is_left_truncatable = [False, False, True, True, False, True, False, True, False, False]
    is_right_truncatable = list(is_left_truncatable)

    dual_truncatable_primes = []
    p = 10
    while len(dual_truncatable_primes) < 11:            # the problem tells us that there are exactly 11 such primes
        if isPrime(p):
            left_truncatable = is_left_truncatable[rm_left(p)]
            is_left_truncatable.append(left_truncatable)

            right_truncatable = is_right_truncatable[rm_right(p)]
            is_right_truncatable.append(right_truncatable)

            if left_truncatable and right_truncatable:
                #print(p)
                dual_truncatable_primes.append(p)
        else:
            is_left_truncatable.append(False)
            is_right_truncatable.append(False)
        
        p += 1
    
    return dual_truncatable_primes

def main():

    #dual_truncatable_primes = brute_force()
    dual_truncatable_primes = dynamic_programming()
    total = sum(dual_truncatable_primes)

    print(f"The sum of sum of the only 11 primes that are both truncatable from left to right and right to left is:", total)
    return total
    
if __name__ == "__main__":
    main()