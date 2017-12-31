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

f = 1
f_list = []
max_f = 1
while f <= int(math.sqrt(600851475143)):
    f += 1
    if isPrime(f):
        print f
        if 600851475143 % f == 0:
            f_list += [f]
            max_f = f

print f_list
print max_f
