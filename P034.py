def factorial(n):
    if n <= 0:
        return 1
    return n*factorial(n-1)

def getDigits(n):
    out = []
    while n != 0:
        out = [n%10] + out
        n /= 10
    return out

fact = []
for i in range(3,1000000):
    D = getDigits(i)
    accum = 0
    for d in D:
        accum += factorial(d)
    print i, accum
    if accum == i:
        fact += [i]

print fact
print sum(fact)
