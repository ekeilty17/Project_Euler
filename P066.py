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

#using a paper by Hendrik W. Lenstra, Jr. http://www.ams.org/notices/200202/fea-lenstra.pdf
# take 14
#   the sqrt(14) can be written as the repeated fraction 3, (1,2,1,6)
#   if we truncate that at the last element in the period you get 3, (1, 2, 1) 
#   evaluating that continued fraction gives 15/4
#   15**2 - 14*(4**2) = 1...and we are done
#   if this is not the case, square the fundamental solution set (15 + 4*sqrt(14)) until it does equal 1


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
def TruncatedFraction(fract):
    
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

def square_fundamental_solution(TF, D):
    a = TF[0]
    b = TF[1]

    return [a*a + D*b*b, 2*a*b]

def Diophantine(D):
    # continued fraction of sqrt(D)
    CF = ContinuedFraction(D)
    
    # The only exception to truncating the fraction
    # is if the length of the period is 1
    if len(CF[1]) == 1:
        CF = [CF[0]] + CF[1]
    else:
        CF = [CF[0]] + CF[1][:-1]
    
    TF = TruncatedFraction(CF)

    # I think you only ever have to square it once, but I am not sure
    while TF[0]**2 - D*TF[1]**2 != 1:
        #print TF[0]**2 - D*TF[1]**2
        #print TF
        TF = square_fundamental_solution(TF, D)

    return TF[0]

D = [0, 0] # the 0,0 part just make the indexes match
for i in range(2,1001):
    d = Diophantine(i)
    D += [d]
    print i,'\t',d,'\t',ContinuedFraction(i)
print
print max(D), D.index(max(D))

