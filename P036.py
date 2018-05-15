def binary(n):
    if n == 0:
        return 0
    return n%2 + 10*binary(n//2)

def getDigits(n):
    out = []
    while n != 0:
        out = [n%10] + out
        n /= 10
    return out

def isPalindrome(n):
    d = getDigits(n)
    if len(d)%2 == 0:
        if d[0:len(d)//2] == list(reversed(d[len(d)//2:])):
            return True
    else:
        if d[0:len(d)//2] == list(reversed(d[len(d)//2+1:])):
            return True
    return False

accum = 0
for i in range(0,1000000):
    if isPalindrome(i) and isPalindrome(binary(i)):
        print i
        accum += i

print
print accum
