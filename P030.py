def digits(n):
    if n < 0:
        return []
    if n == 0:
        return [0]
    out = []
    while n != 0:
        out = [n%10] + out
        n /= 10
    return out

def dig_sum(n,e):
    accum = 0
    d = digits(n)
    for i in d:
        accum += i**e
    return accum

accum = 0
for i in range(2,1000000):
    if i == dig_sum(i,5):
        print i
        accum += i

print
print accum
