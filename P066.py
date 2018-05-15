#My first attempt...too slow
"""
def Diophantine(D):
    #perfect squares have no solution
    if D**0.5 == int(D**0.5):
        return -1

    #x^2 - D*y^2 = 1
    x = 1
    y = 1
    while True:
        if x*x - D*y*y == 1:
            return x
        y += 2
        #since we are trying to minimize x,
        #we want to check all possible y before upping x
        if x*x < D*y*y:
            x += 1
            if x%2 == 0:
                y = 1
            else:
                y = 2
    return -1
"""

#this was a second attempt, but again it's too slow
#I need a whole different method
"""
import math

def getDigits(n):
    out = []
    while n != 0:
        out = [n%10] + out
        n /= 10
    return out

def DigitalSum(n):
    while n >= 10:
        n = sum(getDigits(n))
    return n

#this accurate but very slow for large numbers
def isPerfectSquare(n):
    #easy checks
    if n%10 not in [0, 1, 4, 5, 6, 9]:
        return False
    if DigitalSum(n) not in [1, 4, 7, 9]:
        return False
    if math.sqrt(n) == int(math.sqrt(n)):
        return True
    return False

def Diophantine(D):
    #perfect squares have no solution
    if isPerfectSquare(D):
        return -1
    y = 1
    while True:
        #this is efficient, but inaccurate for large numbers
        #if (1 + D*y*y)**0.5 == int((1 + D*y*y)**0.5):
        if isPerfectSquare(1 + D*y*y):
            return int((1 + D*y*y)**0.5)
        else:
            y += 1
    return -1

max_x = 0
max_idx = -1
for i in range(2,101):
    x = Diophantine(i)
    print i, x
    if x != -1:
        if x > max_x:
            max_x = x
            max_idx = i

print
print "D =",max_idx,"\tx =",max_x
"""

#using a paper by HENDRIK W. LENSTRA, JR.
#take 14
#   the sqrt(14) can be written as the repeated fraction 3, (1,2,1,3) with a period of 4
#   if we truncate that at the last element in the period you get 3, (1, 2, 1) which equals 15/4
#   and 15*15 = 14*4*4 + 1
#   This is true for all numbers

#code from P064 to generate the continued fraction
def ContinuedFraction(n):
    if n**0.5 == int(n**0.5):
        return (int(n**0.5),[0])
    #we iterate on the form (sqrt(n) + a)/b
    #   fract = [a, b]

    #sqrt(n) = (sqrt(n) + 0)/1
    fract = [0, 1]

    #(sqrt(n) + a)/b = y + 1/[ (sqrt(n) -a + b*y)/ ((n - (a-b*y)**2)/b) ]
    out = []
    while True:
        #If b ever equals 1, by definition we have reach the recurrive point
        if fract[1] == 1 and out != []:
            break
        y = int((n**0.5 + fract[0])/fract[1])
        out += [y]
        fract_prev = list(fract)
        a = fract[0]
        b = fract[1]
        fract[0] = -a + b*y
        fract[1] = (n - (a-b*y)**2)/b
    return (out[0], out[1:] + [fract[0] + int(n**0.5)])

def gcd(a, b):
    if b > a:
        a, b = b, a
    while b != 0:
        a, b = b, a%b
    return a

#take code from P065.py to generate the truncated fraction
def TruncatedFraction(n):
    fract = ContinuedFraction(n)
    if len(fract[1]) % 2 == 1:
        fract = [fract[0]] + fract[1]
    else:
        fract = [fract[0]] + fract[1][:-1]

    #accum = [a,b] where f ~ a/b
    accum = [fract[-1], 1]
    for i in range(len(fract)-2,-1,-1):
        a = accum[0]
        b = accum[1]
        accum[0] = fract[i]*a + b
        accum[1] = a
        g = gcd(accum[0],accum[1])
        accum[0] /= g
        accum[1] /= g
    return accum

def Diophantine(D):
    return TruncatedFraction(D)[0]

"""
max_x = 0
max_idx = -1
for i in range(2,1001):
    x = Diophantine(i)
    print i, x
    if x != -1:
        if x > max_x:
            max_x = x
            max_idx = i

print
print "D =",max_idx,"\tx =",max_x
"""

#for i in range(2,100):
    #print i,'\t',Diophantine(i),'\t',ContinuedFraction(i)

print 991,'\t',Diophantine(991),'\t',ContinuedFraction(991)
