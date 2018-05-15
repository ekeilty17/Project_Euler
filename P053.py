def factorial_list(n):
    out = [1]
    accum = 1
    for i in range(1,n+1):
        accum *= i
        out += [accum]
    return out

F = factorial_list(100)

def nCr(n,r):
    return F[n]/(F[r]*F[n-r])

cnt = 0
for n in range(1,101):
    for r in range(1,n+1):
        if nCr(n,r) > 1000000:
            print n,r
            cnt += 1
print
print cnt
