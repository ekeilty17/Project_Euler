def Pentagon(n):
    return (n*(3*n-1))/2

def Pen_inv(x):
    return (1+(24*x+1)**(0.5))/6

def isInt(n):
    if n == int(n):
        return True
    return False

p = []
mx = 10000
#the pair number found with the property will have the smallest difference
for i in range(1,mx):
    for j in range(i+1,mx):
        P_i = Pentagon(i)
        P_j = Pentagon(j)
        print P_i, P_j
        #if P[i]+P[j] in P and P[j]-P[i] in P:
        if isInt(Pen_inv(P_j+P_i)):
            if isInt(Pen_inv(P_j-P_i)):
                p = [i, j]
                break
                break

print
print p[0],p[1]
print Pentagon(p[0]), Pentagon(p[1])
print Pentagon(p[1]) - Pentagon(p[0])
