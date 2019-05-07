from itertools import permutations

def add(a, b=0):
    return a+b

def sub(a, b=0):
    return a-b

def mult(a, b=1):
    return a*b

def div(a, b=1):
    return float(a) / float(b)

def consecutive(L):
    n = 0
    for i in range(len(L)):
        if i+1 == L[i]:
            n += 1
        else:
            break
    return n

L = [add, sub, mult, div]
perm = permutations([0,0,0, 1,1,1, 2,2,2, 3,3,3,], 3)
perm = list(perm)

def Arithmetic(abcd):
    nums = list(permutations(abcd))
    targets = set([])
    for p in perm:
        for n in nums:
            total = L[p[0]]( L[p[1]]( L[p[2]]( n[0], n[1] ), n[2] ), n[3] )
            if int(total) == total and total > 0:
                targets.add( total )

    targets = list(sorted(targets))
    print targets
    return consecutive(targets)

print Arithmetic([1, 2, 3, 5])
