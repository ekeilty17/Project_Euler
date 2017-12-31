import math

def isPrime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n == 3:
        return True
    for i in range(2,int(math.sqrt(n))+1):
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

print nthPrime(10001)
