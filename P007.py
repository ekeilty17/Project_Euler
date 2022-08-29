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

def nthPrime(n):
    if n < 1:
        return 1
    
    counter = 0
    candidate = 1
    while counter < n:
        candidate += 1
        if isPrime(candidate):
            counter += 1
    return candidate

def main(N=10001):

    p = nthPrime(N)

    print(f"The {N} prime number:", p)
    return p

if __name__ == "__main__":
    main(10001)