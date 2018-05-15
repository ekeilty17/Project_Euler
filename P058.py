def isPrime(n):
    if n <= 0:
        return False
    if n == 1:
        return False
    first_few = [      2,   3,   5,   7,  11,  13,  17,  19,  23,  29,  31,  37,  41,  43,  47,
                      53,  59,  61,  67,  71,  73,  79,  83,  89,  97, 101, 103, 107, 109, 113,
                     127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]
    if n in first_few:
        return True
    for i in range(2,int(n**(0.5))+1):
        if n % i == 0:
            return False
    return True

#this brute forces it, but it's too slow
"""
#to add to a list in a spiral fashion
def add_right(L,a):
    for i in range(0,len(a)):
        L[i] += [a[i]]
    return L

def add_bottom(L,a):
    return L + [list(reversed(a))]

def add_left(L,a):
    a = list(reversed(a))
    for i in range(0,len(a)):
        L[i] = [a[i]] + L[i]
    return L

def add_top(L,a):
    return [a] + L

#generates nxn spiral (n can only be odd)
def gen_spiral(n):
    if n <= 0:
        return []
    if n % 2 == 0:
        return []
    if n == 1:
        return [[1]]
    out = gen_spiral(n-2)
    nxt = out[0][len(out[0])-1] + 1

    out = add_right(out,range(nxt,nxt+n-2))
    nxt += n-2

    out = add_bottom(out,range(nxt,nxt+n-1))
    nxt += n-1

    out = add_left(out,range(nxt,nxt+n-1))
    nxt += n-1

    out = add_top(out,range(nxt,nxt+n))

    return out

def add_spiral(L):
    out = list(L)
    n = len(L)+2
    nxt = out[0][len(out[0])-1] + 1

    out = add_right(out,range(nxt,nxt+n-2))
    nxt += n-2

    out = add_bottom(out,range(nxt,nxt+n-1))
    nxt += n-1

    out = add_left(out,range(nxt,nxt+n-1))
    nxt += n-1

    out = add_top(out,range(nxt,nxt+n))

    return out

def getDiag(L):
    out = []

    #top left to bottom right
    for i in range(0,len(L)):
        out += [L[i][i]]

    #bottom left to top right
    for i in range(0,len(L)):
        if i != len(L)//2:
            out += [L[len(L)-i-1][i]]

    return out

spiral = gen_spiral(3)
diag = [1]
cnt = 1
n = 3
while cnt/float(len(diag)) > 0.1:
    cnt = 0
    spiral = add_spiral(spiral)
    diag = getDiag(spiral)
    for d in diag:
        if isPrime(d):
            cnt += 1
    print n,cnt,len(diag),cnt/float(len(diag))
    n += 2
"""

#instead, let's just get a formula for the number on each diagonal
def diag(n):
    if n == 1:
        return [1]
    return [n*n-3*(n-1), n*n-2*(n-1), n*n-1*(n-1), n*n-0*(n-1)]

num_prime = 3
total = 5
n = 5
while num_prime/float(total) > 0.1:
    print n,num_prime,total,num_prime/float(total) 
    D = diag(n)
    for d in D:
        if isPrime(d):
            num_prime += 1
    total += 4
    n += 2

