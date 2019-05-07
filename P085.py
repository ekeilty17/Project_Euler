
# Number of rectanges of a given size (kn by km) that fit in a rectangle of size n by m
def subR(n, m, kn, km):
    return (n - (kn-1)) * (m - (km-1))

# R = SUM{ SUM{ subR } } kn = 1 --> n, km = 1 --> m
def R(n, m):
    accum = 0
    for kn in range(1, n+1):
        for km in range(1, m+1):
            accum += subR(n, m, kn, km)
    return accum

N = 2*10**6
closest = abs(N - R(1, 1))
closest_r = [1, 1]

"""
# Too inefficient
for i in range(1, 2000):
    for j in range(i, 2000):
        print i, j
        r = R(i, j)
        if abs(N - r) < closest:
            closest = abs(N - r)
            closest_r = [i, j]
"""

i = 1
j = 1
r = R(i, j)
while r <= N:
    while r <= N:
        j += 1
        print i, j
        r = R(i, j)
        if abs(N - r) < closest:
            closest = abs(N - r)
            closest_r = [i, j]
    i += 1
    j = i
    r = R(i, j)

print
print closest_r[0], closest_r[1]
print R(closest_r[0], closest_r[1])
print closest_r[0] * closest_r[1]
