def getDigits(n):
    out = []
    while n != 0:
        out = [n%10] + out
        n /= 10
    return out

#instead of writing a general function
#I'm assuming 3 numbers
def isPerm_3(n1, n2, n3):
    if list(sorted(getDigits(n1))) == list(sorted(getDigits(n2))) == list(sorted(getDigits(n3))):
        return True
    return False

def isPrime(n):
    if n <= 0:
        return False
    if n == 1:
        return False
    first_few = [      2,   3,   5,   7,  11,  13,  17,  19,  23,  29,  31,  37,  41,  43,  47,
                      53,  59,  61,  67,  71,  73,  79,  83,  89,  97, 101, 103, 107, 109, 113,
                     127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]
    if n in first_few:
        return True
    for i in range(2,int(n**(0.5))+1):
        if n % i == 0:
            return False
    return True

def get_stuff():
    found = False
    while not found:
        for i in range(1000,10001):
            if isPrime(i):
                add = 1000
                nxt_1 = i+add
                nxt_2 = i+add+add
                while nxt_2 < 10001:
                    nxt_1 = i+add
                    nxt_2 = i+add+add
                    print i,nxt_1,nxt_2
                    if (isPerm_3(i, nxt_1, nxt_2) and isPrime(nxt_1) and isPrime(nxt_2)) and i != 1487:
                        print
                        print i,nxt_1,nxt_2
                        return [i,nxt_1,nxt_2]
                    add += 1

get_stuff()

