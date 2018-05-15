import math

for a in range(0,500):
    for b in range(0,500):
        c = math.sqrt(a**2+b**2)
        if a+b+c == 1000:
            print "a =",a
            print "b =",b
            print "c =",c
            print "abc =",a*b*c
            break
