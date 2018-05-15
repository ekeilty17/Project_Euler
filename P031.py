#not very efficient, but not really sure how else to solve it

money   = [  1,   2,  5, 10, 20, 50, 100]
mx      = [200, 100, 40, 20, 10,  4,   2]
coef    = []

n = 200

for a in range(0,mx[0]+1):
    for b in range(0,mx[1]+1):
        for c in range(0,mx[2]+1):
            for d in range(0,mx[3]+1):
                for e in range(0,mx[4]+1):
                    for f in range(0,mx[5]+1):
                        for g in range(0,mx[6]+1):
                            if a*money[0] + b*money[1] + c*money[2] + d*money[3] + e*money[4] + f*money[5] + g*money[6] == 200:
                                print a,b,c,d,e,f,g
                                coef += [[a,b,c,d,e,f,g]]

print len(coef)
