def numDigits(n):
    accum = 0
    while n != 0:
        accum += 1
        n /= 10
    return accum

b = 1
e = 1
cnt = 0
found = False
while not found:
    if numDigits(b**e) == e:
        print b,e,b**e
        cnt += 1
    if numDigits(b**e) > e:
        b = 1
        e += 1
    else:
        b += 1
    #I can't prove for certain that there doesnt exist any above e==100
    #it just seemed like a reasonable upper bound
    if e == 100:
        found = True

print
print cnt
