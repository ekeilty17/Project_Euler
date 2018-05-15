#It you look at it mathematically, it turns out the answer is just 2nCn
#nCr = n!/r!(n-r!)

def factorial(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n < 0:
        return 0
    accum = 1
    for i in range(1,n+1):
        accum *= i
    return accum

def Lattice_paths(n):
    return factorial(2*n)/(factorial(n)*factorial(2*n-n))

print Lattice_paths(20)
