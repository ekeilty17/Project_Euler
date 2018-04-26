def divisors(n):
    if n <= 0:
        return []
    if n == 1:
        return []
    if n == 2:
        return [1,2]
    f = [1]
    for i in range(2,n//2+1):
        if n%i == 0:
            f += [i]
    return f

def isAbundant(n):
    if sum(divisors(n)) > n:
        return True
    return False

abundant = []
for i in range(0,28124/2+1):
    if isAbundant(i):
        abundant += [i]


