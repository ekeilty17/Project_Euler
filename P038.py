def numDigits(n):
    cnt = 0
    while n != 0:
        n /= 10
        cnt += 1
    return cnt

def getDigitList(n):
    out = []
    while n != 0:
        out = [n%10] + out
        n /= 10
    return out

def concat(L):
    accum = 0
    for i in range(0,len(L)):
        accum *= 10
        accum += L[i]
    return accum

mx = []
for n in range(1,10000):
    dig = []
    for i in range(1,10):
        dig += getDigitList(i*n)
        if list(sorted(dig)) == [1,2,3,4,5,6,7,8,9]:
            print dig, n
            mx = dig
            break

print
print mx
print concat(mx)
