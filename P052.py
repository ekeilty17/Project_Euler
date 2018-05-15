def getDigits(n):
    out = []
    while n != 0:
        out = [n%10] + out
        n /= 10
    return out

found = False
x = 0
while not found:
    x += 1
    print x
    found = True
    D = list(sorted(getDigits(x)))
    for i in range(2,7):
        if list(sorted(getDigits(i*x))) != D:
            found = False
            break

print
for i in range(1,7):
    print i*x
