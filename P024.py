#a function that will generate all lexicographic permutations for a given number
"""
def lex(n):
    if n == 0:
        return [[0]]
    if n == 1:
        return [[0, 1], [1, 0]]
    n_1 = lex(n-1)
    out = []
    for sL in n_1:
        for i in range(len(sL),-1,-1):
            out += [ sL[0:i] + [n] + sL[i:] ]
    return out

#brute force
Lex_9 = sorted(lex(9))
print Lex_9[999999]
"""

#this one lends itself to thinking mathematically a bit before
#rather than a strictly brute force approach

#permutation 0987654321 is permutation 1*9! = 362,880
#permutation 1987654320 is permutation 2*9! = 725,760
#permutation 2987654310 is permutation 3*9! = 1,088,640

#so the 1 millionth permutation begins with a 2

#perm 725,760 = 1987654320
#perm 725,761 = 2013456789
#1,000,000 - 725,760 = 274,240
#need to find the 274,240th lexicographic permutation of digits
#       0, 1, 3, 4, 5, 6, 7, 8, 9

"""
Lex_8 = sorted(lex(8))
perm_8d_274240 = Lex_8[274240 - 1]

for i in range(len(perm_8d_274240)):
    if perm_8d_274240[i] > 1:
        perm_8d_274240[i] += 1

perm_9d_1000000 = [2] + perm_8d_274240
print perm_9d_1000000
"""

#Continuing to use this logic to deduce the solution
def factorial(n):
    if n <= 0:
        return 1
    if n == 1:
        return 1
    return n*factorial(n-1)

n = 1000000

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
out = []
for i in range(9,0,-1):
    f = factorial(i)
    i = 1
    while i*f < n:
        i += 1
    out += [nums[i-1]]
    del nums[i-1]
    n -= (i-1)*f

out += nums

print out
