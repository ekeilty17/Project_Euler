def isCyclic(n,m):
    s_n = str(n)
    s_m = str(m)
    if len(s_n) < 2 or len(s_m) < 2:
        return False
    if s_n[len(s_n)-2:] == s_m[:2]:
        return True
    else:
        return False

def isSetCyclic(S):
    for i in range(0,len(S)-1):
        if isCyclic(S[i],S[i+1]) == False:
            return False
    if isCyclic(S[len(S)-1], S[0]):
        return True
    else:
        return False

def is4digits(n):
    s_n = str(n)
    if len(s_n) == 4:
        return True
    else:
        return False

def P(k,n):
    if k == 3:
        return (n*(n+1))/2
    elif k == 4:
        return n*n
    elif k == 5:
        return (n*(3*n-1))/2
    elif k == 6:
        return n*(2*n-1)
    elif k == 7:
        return (n*(5*n-3))/2
    elif k == 8:
        return n*(3*n-2)
    else:
        return 0

"""
#find the range of 4 digit numbers
for i in range(3,9):
    a = 1
    n_a = 1
    while is4digits(a) == False:
        a = P(i,n_a+1)
        n_a += 1
    print n_a,P(i,n_a)
"""
#output of ^
#45 1035
#32 1024
#26 1001
#23 1035
#21 1071
#19 1045

k = [3,5,4]

n_S_original = [45,32,26]
n_S = [45,32,26]
S = [P(k[0],n_S[0]), P(k[1],n_S[1]), P(k[2],n_S[2])]

"""
n_S = [45,32,36,23,21,19]
S = [P(3,n_S[0]), P(4,n_S[1]), P(5,n_S[2]), P(6,n_S[3]), P(7,n_S[4]), P(8,n_S[5])]
"""

ref = 0
while ref < len(S):
    print S
    #if element after ref has more than 5 digits,
    #we have to start from the beginning with n_S[0] upped by 1
    if is4digits(S[(ref+1)%len(S)]) == False:
        n_S[0] += 1
        n_S[1:] = n_S_original[1:] 
        S = [P(k[0],n_S[0]), P(k[1],n_S[1]), P(k[2],n_S[2])]
        ref = 0

    if is4digits(S[ref]) == False:
        if ref != 0:
            ref -= 1
        else:
            break

    #if we found pairs that are cyclic, then the ref is uped by 1
    #else we go to the next number in the sequence in ref+1
    if isCyclic(S[ref],S[(ref+1)%len(S)]):
        ref += 1
    else:
        S[(ref+1)%len(S)] = P(((ref+1)%len(S))+3,n_S[(ref+1)%len(S)]+1)
        n_S[(ref+1)%len(S)] += 1

    if isSetCyclic(S):
        break

print S
print n_S
