def getDigits(n):
    out = []
    while n != 0:
        out = [n%10] + out
        n /= 10
    return out

def factorial(n):
    L = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
    return L[n]

def DigitFactorial(n):
    return sum(map(factorial, getDigits(n)))

def Chain(n):
    d = DigitFactorial(n)
    out = [n]
    while d not in out:
        out += [d]
        d = DigitFactorial(d)
    return out

accum = []
for i in range(0, 1000000):
    C = Chain(i)
    print i, len(C)
    if len(C) == 60:
        accum += [i]

print len(accum)
