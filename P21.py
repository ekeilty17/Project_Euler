def factors(n):
    if n < 0:
        return []
    if n == 0:
        return []
    if n == 1:
        return [1]
    f = [1]
    for i in range(2,n//2+1):
        if n % i == 0:
           f += [i]
    return f

def d(n):
    return sum(factors(n))

def isAmicable(a):
    b = d(a)
    if a == b:
        return False
    if a == d(b):
        return True
    else:
        return False


amicable = []
for i in range(1,10001):
    if isAmicable(i):
        amicable += [i]

print amicable
print sum(amicable)
