from collections import defaultdict 

def getDigits(n):
    return [int(d) for d in str(n)]

def numDigits(n):
    return len(str(n))

def isPandigital(a, b, N):
    digits_used = getDigits(a) + getDigits(b) + getDigits(a*b)
    return sorted(digits_used) == list(range(1, N+1))

# The brute force is actually pretty fast
def brute_force(N):

    pandigital_products = defaultdict(list)
    
    for a in range(1, 10**(N//2)):
        for b in range(a+1, 10**(N+1)):
            if numDigits(a) + numDigits(b) + numDigits(a*b) > N:        # This is actually a critical pruning step because it means we don't have to sort
                break
            if isPandigital(a, b, N):
                pandigital_products[a*b] += [(a, b)]
    
    return sum(pandigital_products.keys())
    #return len(pan)

def main(N=9):
    
    total = brute_force(N)

    print(f"The sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through {N} pandigital is:", total)
    return total

if __name__ == "__main__":
    main()