def factorial(n):
    if n < 0:
        return
    if n == 0:
        return 1
    return n*factorial(n-1)

def sum_factorial(n):
    s = str(factorial(n))
    accum = 0
    for d in s:
        accum += int(d)
    return accum

print sum_factorial(100)
