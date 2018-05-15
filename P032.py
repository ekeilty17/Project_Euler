#gets digits of a number
def getDigits(n):
    out = []
    while n != 0:
        out = [n%10] + out
        n /= 10
    return out

#gets number of digits of a number
def numDigits(n):
    cnt = 0
    while n != 0:
        n /= 10
        cnt += 1
    return cnt

#a*b
def isPandigital(a,b):
    out = getDigits(a) + getDigits(b) + getDigits(a*b)
    if sorted(out) == [1,2,3,4,5,6,7,8,9]:
        return True
    return False

pan = []
i = 1
while i < 10000:
    j = i
    while j < 987654322:
        if numDigits(i) + numDigits(j) + numDigits(i*j) > 9:
            break
        if isPandigital(i,j):
            print i,j,i*j
            if i*j not in pan:
                pan += [i*j]
        j += 1
    i += 1

print sum(pan)
