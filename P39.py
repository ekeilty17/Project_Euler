import math

def isInt(n):
    if n == int(n):
        return True
    else:
        return False

def Pyth(a,b):
    return math.sqrt(a*a + b*b)

a = 1
b = 1
P = []
while a < 500:
    #this is so I don't double count
    if a < b:
        c = Pyth(a,b)
        if isInt(c):
            if a+b+c <= 1000:
                P += [a+b+c]
                print a,b,c
    if b == 500:
        a += 1
        b = 1
    else:
        b += 1

print
print P

#idk let's make a sorting algorithm for fun
for i in range(0,len(P)-1):
    for j in range(0,len(P)-1-i):
        if P[j+1] < P[j]:
            temp = P[j]
            P[j] = P[j+1]
            P[j+1] = temp

print
print P

most = 0
counter = 0
max_P = 0
for i in range(0,len(P)-1):
    if P[i] == P[i+1]:
        counter += 1
        if counter > most:
            most = counter
            max_P = P[i]
    else:
        counter = 0

print max_P
