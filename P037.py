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

def numDigits(n):
    cnt = 0
    while n != 0:
        n /= 10
        cnt += 1
    return cnt

def rm_left(n):
    return n % (10**(numDigits(n)-1))

def rm_right(n):
    return n/10

def isTruncatable_left(p):
    while p != 0:
        if not isPrime(p):
            return False
        p = rm_left(p)
    return True

def isTruncatable_right(p):
    while p != 0:
        if not isPrime(p):
            return False
        p = rm_right(p)
    return True

cnt = 0
p = 11
trun = []
while cnt < 11:
    #to limit the search:
    #the right-most digit cannot be equal to [0, 1, 2, 4, 5, 6, 8, 9]
    #the left-most digit cannot be equal to [1, 4, 6, 8, 9] 
    if p%2 != 0 and p%10 != 1 and p%10 != 5 and p%10 != 9 and (p/(10**(numDigits(p)-1))) not in [0,1,4,6,8,9]:
        if isTruncatable_left(p) and isTruncatable_right(p):
            print p
            trun += [p]
            cnt += 1
            #this is if you only wanted to include the largest version of the truncatable number
            """
            for i in range(0,len(trun)-1):
                if trun[i] == rm_left(p) or trun[i] == rm_right(p):
                    del trun[i]
                    break
            """
    p += 1

print trun
print sum(trun)
