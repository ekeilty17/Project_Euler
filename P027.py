def isPrime(n):
    if n <= 0:
        return None
    if n == 1:
        return False
    first_few = [      2,   3,   5,   7,  11,  13,  17,  19,  23,  29,  31,  37,  41,  43,  47, 
                      53,  59,  61,  67,  71,  73,  79,  83,  89,  97, 101, 103, 107, 109, 113, 
                     127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]
    if n in first_few:
        return True
    for i in range(2,int(n**(0.5))+1):
        if n % i == 0:
            return False
    return True

n = 0
max_string_primes = 0
num = []
cnt = 0

for a in range(-1000,1001):
    for b in range(-1000,1001):
        print a,b
        n = 0
        cnt = 0
        while True:
            if isPrime(n**2 + a*n + b):
                cnt += 1
            else:
                break
            n += 1
        if cnt > max_string_primes:
            max_string_primes = cnt
            num = [a,b]

print  num,max_string_primes
print num[0] * num[1]
