def Triangle(n):
   return n*(n+1)/2

def Pentagon(n):
    return n*(3*n-1)/2

def Hexagon(n):
    return n*(2*n-1)

def Pen_inv(x):
    return (1 + (24*x+1)**(0.5))/6

def Hex_inv(x):
    return (1 + (8*x+1)**(0.5))/4

def isInt(n):
    if n == int(n):
        return True
    return False

#this brute forces it, but it takes too long
"""
#T_n = 285
#P_n = 165
#H_n = 143
T_n = 1
P_n = 1
H_n = 1
found = False

while not found:
    T_n += 285
    P_n = 165
    H_n = 143
    while Pentagon(P_n) <= Triangle(T_n):
        H_n = 143
        while Hexagon(H_n) <= Pentagon(P_n):
            print Triangle(T_n), Pentagon(P_n), Hexagon(H_n)
            if Triangle(T_n) == Pentagon(P_n) == Hexagon(H_n):
                found = True
                break
            H_n += 1
        P_n += 1
"""

T_n = 286
found = False
while not found:
    x = Triangle(T_n)
    print x
    if isInt(Pen_inv(x)) and isInt(Hex_inv(x)):
        print
        print x
        break
    T_n += 1
