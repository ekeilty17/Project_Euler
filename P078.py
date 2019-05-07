
# Using the recurrance relation:
#   p(n) = p(n-1) + p(n-2) - p(n-5) - p(n-7) + p(n-12) + p(n-15) - ...
#       pattern of signs are ++ -- ++ -- ...
#       1, 2, 5, 7, 12, 15, are the generalized pentagon numbers
#   p(n) = SUM{ (-1)^(floor(m/2)) * p(n - g(m)) } for 0 <= m <= n
#   where g(k) are the generalized pentagonal numbers

# 1, 2, 5, 7, 12, 15, ... comes from k = 0, 1, -1, 2, -2, 3, ...
def Pent(k):
    return (3*k**2 - k)/2

# This converts 0, 1, 2, 3, 4, ... to 0, 1, -1, 2, -2, ...
def k(m):
    if m % 2 == 0:
        return -m/2
    else:
        return m/2 + 1

# Really slow
def P1(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    if n == 1:
        return 1
    
    accum = 0
    m = 1
    while Pent(k(m)) <= n:
        accum += (-1)**((m-1)//2) * P1(n - Pent(k(m)))
        m += 1
    return accum

p = [1, 1]
def P(n):
    if n < 0:
        return 0
    if n < len(p):
        return p[n]
    accum = 0
    m = 1
    while Pent(k(m)) <= n:
        accum += (-1)**((m-1)//2) * P(n - Pent(k(m)))
        accum %= N
        m += 1
    return accum

n = 2
N = 10**6
while True:
    print n, p[-1]
    p += [P(n)]
    if p[-1] % N == 0:
        break
    n += 1

print
print "First number for which its partitions are divisible by", N, "is", n, "with P(n) =", p[-1]
