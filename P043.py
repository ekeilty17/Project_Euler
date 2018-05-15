def allPandigital(n):
    if n == 0:
        return [[0]]
    if n == 1:
        return [[0, 1], [1,0]]
    n_1 = allPandigital(n-1)
    out = []
    for sL in n_1:
        for i in range(len(sL),-1,-1):
            out += [ sL[0:i] + [n] + sL[i:] ]
    return out

def numberify(L):
    accum = 0
    for i in range(0,len(L)):
        accum *= 10
        accum += L[i]
    return accum

pan = allPandigital(9)
accum = 0
for p in pan:
    if  numberify(p[1:4]) % 2 == 0 and numberify(p[2:5]) % 3 == 0 and numberify(p[3:6]) % 5 == 0 and numberify(p[4:7]) % 7 == 0 and numberify(p[5:8]) % 11 == 0 and numberify(p[6:9]) % 13 == 0 and numberify(p[7:10]) % 17 == 0:
        accum += numberify(p)
        print numberify(p)

print accum
