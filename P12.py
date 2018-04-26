def Triangle(n):
    accum = 0
    for i in range(1,n+1):
        accum += i
    return accum

def factors(n):
    if n == 0:
        return []
    if n < 0:
        n *= -1
    if n == 1:
        return [1]
    f = [1,n]
    for i in range(2,n//2+1):
        if n % i == 0:
            f += [i]
    return sorted(f)

"""
f = []
x = 1
while len(f) < 5:
    x += 1
    print x
    f = factors(Triangle(x))
"""
#the above technically works, but its way too slow

#Improvements:
#   instead of using a function to compute the Triangle numbers,
#       we compute along with the while loop
#   the factors function is also pretty slow, we don't need to actually find the factors
#       we just need to find the number, which is much faster

def num_factors(n):
    f = 1
    counter = 0
    while n % 2 == 0:
        counter += 1
        n = n/2
    f *= (counter + 1)
    p = 3
    while n != 1:
        counter = 0
        while n % p == 0:
            counter += 1
            n /= p
        f *= (counter + 1)
        p += 2
    return f

f = 0
T = 1
x = 1
while f < 500:
    T += x + 1
    x += 1
    f = num_factors(T)
    print T, f

print
print T
print num_factors(T)
