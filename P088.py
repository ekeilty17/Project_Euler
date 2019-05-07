from math import log

# Definitions
#   (x1, x2, ..., xn) is a set of numbers s.t. x1 + x2 + ... + xn = x1 * x2 * ... * xn
#   a(n) is the number of sets s.t. the above is true for a given n (length of that set)

# Some Theorems
#   if x1 + ... + xn = 2n, then (x1, x2, ..., xn) = (1, 1, ..., 1, 2, n)]
#   if n is even, then a solution (x1, x2, ..., xn) must be divisible by 4
#   let bn = number of 1's in (x1, x2, ..., xn)
#       bn >= n - 1 - [log2(n)]
#   if a(n) = 1, then n-1 is prime
#   if a(n) = 1 and n >= 4, then 2|n
#   if a(n) = 1 and n >= 5, then 3|n
#   if a(n) = 1 and n >= 5, then 6|n
#   if a(n) = 1 and n > 100, then n = 7k or n = 7k+2 or n = 7k+3 or n = 7k+6 for k>=14
#   if a(n) = 1 and n > 100, then n 30k or n = 30k+24 for k >= 3

# Conjectures
#   if a(n) = 1 and n >= 5, then n = 30k + 24
#   if a(n) = 1 and n > 100, then n = 114, 174, 444

def P(L):
    return reduce((lambda x, y: x*y), L)

# This totally works...it's just too slow :(
# I'm pretty proud of the algorithm tho
"""
def Product_Sums(k):
    
    if k == 2:
        return sum([2, 2])

    # exploiting number of 1's in (x1, x2, ..., xn) >= n - 1 - [log2(n)]
    b = k - 1 - int(log(k, 2))

    L = [1]*(k-2) + [2, 2]
    prev_inc = len(L)-1
    
    min_L = []
    min_sum = -1
    while L.count(1) >= b:
        while P(L) <= sum(L):
            if P(L) == sum(L):
                if min_sum == -1:
                    min_L = list(L)
                    min_sum = sum(L)
                elif sum(L) < min_sum:
                    min_L = list(L)
                    min_sum = sum(L)
            L[-1] += 1
            prev_inc = len(L)-1
        
        L[prev_inc-1] += 1
        L[prev_inc:] = [L[prev_inc-1]]*(len(L) - prev_inc)
        prev_inc -= 1
    
    print min_L
    return min_sum

k = 12000
PS_set = set([])
for i in range(2, k+1):
    s = Product_Sums(i)
    print i, s
    PS_set.add(s)
print
print sum(PS_set)

"""

# As always with these problems, I suspect the trick is you don't actually need to find the list itself, you only need to find its sum/product


