#produce numbers
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

#produce permutations
def Lex(n):
    if n == 0:
        return [[0]]
    if n == 1:
        return [[0, 1], [1, 0]]
    n_1 = Lex(n-1)
    out = []
    for sL in n_1:
        for i in range(len(sL),-1,-1):
            out += [ sL[0:i] + [n] + sL[i:] ]
    return out

#given a specific ordering of a set, is the set cyclic
def isCyclic_order(S):
    for i in range(0,len(S)):
        if str(S[i%len(S)])[-2:] != str(S[(i+1)%len(S)])[:2]:
            return False
    return True

#It wouldn't be hard to make a general cyclic formula by putting the Lex funciton in the cyclic function, 
#but I'm trying save on computation time, so I made a specific one
lex_6 = Lex(5)
lex_5 = Lex(4)
def isCyclic_6(S):
    for perm in lex_6:
        new_S = [S[perm[0]],S[perm[1]],S[perm[2]],S[perm[3]],S[perm[4]],S[perm[5]]]
        if isCyclic_order(new_S):
            return True
    return False


#given a specific ordering of a set, is it linearly cyclic
def isLinearlyCyclic_order(S):
    for i in range(0,len(S)-1):
        if str(S[i])[-2:] != str(S[(i+1)])[:2]:
            return False
    return True

def isLinearlyCyclic_5(S):
    for perm in lex_5:
        new_S = [S[perm[0]],S[perm[1]],S[perm[2]],S[perm[3]],S[perm[4]]]
        if isLinearlyCyclic_order(new_S):
            return True
    return False


def isPairCyclic(a,b):
    if str(a)[-2:] == str(b)[:2] or str(b)[-2:] == str(a)[:2]:
        return True
    return False

def isAdditionCyclic(S, d):
    if isPairCyclic(S[0],d):
        return True
    elif isPairCyclic(S[1],d):
        return True
    elif isPairCyclic(S[2],d):
        return True
    else:
        return False

def isPairCyclicExist_3(S):
    if isPairCyclic(S[0],S[1]):
        return True
    elif isPairCyclic(S[1],S[2]):
        return True
    elif isPairCyclic(S[2],S[0]):
        return True
    else:
        return False


def stuff():
    #first find smallest 2 digit number in each P(k,n)
    a_0 = 0
    while P(3,a_0) < 1000:
        a_0 += 1
    b_0 = 0
    while P(4,b_0) < 1000:
        b_0 += 1
    c_0 = 0
    while P(5,c_0) < 1000:
        c_0 += 1
    d_0 = 0
    while P(6,d_0) < 1000:
        d_0 += 1
    e_0 = 0
    while P(7,e_0) < 1000:
        e_0 += 1
    f_0 = 0
    while P(8,f_0) < 1000:
        f_0 += 1
    
    #finding maximum in each set
    a_f = a_0
    while P(3,a_f) < 10000:
        a_f += 1
    b_f = b_0
    while P(4,b_f) < 10000:
        b_f += 1
    c_f = c_0
    while P(5,c_f) < 10000:
        c_f += 1
    d_f = d_0
    while P(6,d_f) < 10000:
        d_f += 1
    e_f = e_0
    while P(7,e_f) < 10000:
        e_f += 1
    f_f = f_0
    while P(8,f_f) < 10000:
        f_f += 1
    
    a_f -= 1
    b_f -= 1
    c_f -= 1
    d_f -= 1
    e_f -= 1
    f_f -= 1

    print P(3,a_0),P(3,a_f)
    print P(4,b_0),P(4,b_f)
    print P(5,c_0),P(5,c_f)
    print P(6,d_0),P(6,d_f)
    print P(7,e_0),P(7,e_f)
    print P(8,f_0),P(8,f_f)
    
    #some key observations: say I have a set of 6 cyclic numbers
    #   if I remove one (now having 5) they will be linearly cyclic
    #   if I remove another (now having 4) there is one of 2 senarios
    #       two sets of 2 linearly cyclic numbers or one set of 4 linearly cyclic numbers
    #   If I remove another (now having 3) I will at least have two linearly cyclic numbers

    #to check 5 case: check that the set is linearly cyclic
    #to check 3 case: check that there exists a pair of two linearly cyclic in the set of 3
    #to check 4 case: check that the additional number (d) is linealy cyclic with at least 1 other number from the previous set of 3

    for a in range(a_0,a_f):
        for b in range(b_0,b_f):
            for c in range(c_0,c_f):
                for d in range(d_0,d_f):
                    if not isPairCyclicExist_3([P(3,a),P(4,b),P(5,c)]):
                        break
                    for e in range(e_0,e_f):
                        print P(3,a), P(4,b), P(5,c), P(6,d), P(7,e)
                        if not isAdditionCyclic([P(3,a), P(4,b), P(5,c)], P(6,d)):
                            break
                        for f in range(f_0,f_f):
                            print P(3,a), P(4,b), P(5,c), P(6,d), P(7,e), P(8,f)
                            if not isLinearlyCyclic_5([P(3,a), P(4,b), P(5,c), P(6,d), P(7,e)]):
                                break
                            if isCyclic_6([P(3,a), P(4,b), P(5,c), P(6,d), P(7,e), P(8,f)]):
                                return [[a,b,c,d,e,f],[P(3,a), P(4,b), P(5,c), P(6,d), P(7,e), P(8,f)]]
    return []

L = stuff()
print
print L[0]
print L[1]
print sum(L[1])

#old attempt
"""
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

#find the range of 4 digit numbers
for i in range(3,9):
    a = 1
    n_a = 1
    while is4digits(a) == False:
        a = P(i,n_a+1)
        n_a += 1
    print n_a,P(i,n_a)
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

#n_S = [45,32,36,23,21,19]
#S = [P(3,n_S[0]), P(4,n_S[1]), P(5,n_S[2]), P(6,n_S[3]), P(7,n_S[4]), P(8,n_S[5])]

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
"""
