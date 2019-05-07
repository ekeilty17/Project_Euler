from itertools import permutations 

def distance_squared(C1, C2):
    (x1, y1) = C1
    (x2, y2) = C2
    return (x2-x1)**2 + (y2-y1)**2

def isRight(C1, C2, C3):
    S = list(sorted([distance_squared(C1, C2), distance_squared(C2, C3), distance_squared(C3, C1)]))
    
    return S[0] + S[1] == S[2]

k = 50
perm = permutations(range(k+1), 2)
perm = list(perm)

for i in range(1, k+1):
    perm += [(i, i)]

cnt = 0
for i in range(len(perm)): 
    for j in range(i+1, len(perm)):
        if isRight((0, 0), perm[i], perm[j]):    
            print perm[i], perm[j]
            cnt += 1
print
print cnt
