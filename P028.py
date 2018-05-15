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
    print n
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

#sums the diagonals
def sum_diag(L):
    accum = 0

    #top left to bottom right
    for i in range(0,len(L)):
        accum += L[i][i]

    #bottom left to top right
    for i in range(0,len(L)):
        if i != len(L)//2:
            accum += L[len(L)-i-1][i]
    
    return accum


out = gen_spiral(1001)

#for r in out:
    #print r
print
s = sum_diag(out)
print s
