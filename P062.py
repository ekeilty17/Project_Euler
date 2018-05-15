def getDigits(n):
    out = []
    while n != 0:
        out = [n%10] + out
        n /= 10
    return out

cubes = []
found = False
i = 1
while not found:
    print i**3
    nxt = getDigits(i**3)
    cubes = [nxt] + cubes
    cnt = 0
    for j in range(0,len(cubes)):
        if list(sorted(cubes[j])) == list(sorted(nxt)):
            cnt += 1
        if len(nxt) > len(cubes[j]):
            break
    if cnt == 5:
        print
        for j in range(0,len(cubes)):
            if list(sorted(cubes[j])) == list(sorted(nxt)):
                print cubes[j]
        found = True
    i += 1

#as much as it annoys me, the below method takes too long, I need a different approach
"""
def getDigits(n):
    out = []
    while n != 0:
        out = [n%10] + out
        n /= 10
    return out

def numDigits(n):
    accum = 0
    while n != 0:
        accum += 1
        n /= 10
    return accum

def isPermutation(S):
    for i in range(1,len(S)):
        if list(sorted(getDigits(S[0]))) != list(sorted(getDigits(S[i]))):
            return False
    return True

def stuff():
    n = 10000
    #two things we can check for to make more efficient
    #   1) if number of digits are not equal, they cannot be permutations
    #   2) if they are not permutations, we don't have to keep iterating
    for a in range(1,n-4):
        for b in range(a+1,n-3):
            if numDigits(b) > numDigits(a):
                break
            for c in range(b+1,n-2):
                print a**3,b**3,c**3
                if numDigits(c) > numDigits(b):
                    break
                if not isPermutation([a**3,b**3]):
                    break
                for d in range(c+1,n-1):
                    print a**3,b**3,c**3,d**3
                    if numDigits(d) > numDigits(c):
                        break
                    if not isPermutation([a**3,b**3,c**3]):
                        break
                    for e in range(d+1,n):
                        print a**3,b**3,c**3,d**3,e**3
                        if numDigits(d) > numDigits(e):
                            break
                        if not isPermutation([a**3,b**3,c**3,d**3]):
                            break
                        if isPermutation([a**3,b**3,c**3,d**3,e**3]):
                            return [a,b,c,d,e]
    return [-1,-1,-1,-1,-1]

L = stuff()
print
print L[0],L[1],L[2],L[3],L[4]
print L[0]**3,L[1]**3,L[2]**3,L[3]**3,L[4]**3
"""
