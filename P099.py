from math import log

# preparing the matrix to make it usable
f=open("p099_base_exp.txt",'r')

L = []
lines = f.readlines()
for line in lines:
    L += [line.split('\n')[0].split(',')]

f.close()

for i in range(len(L)):
    L[i][0] = int(L[i][0])
    L[i][1] = int(L[i][1])

# Using the fact that log(x^b) = b*log(x)
# and obviously taking the log of both sides will not change the inequality

max_val = L[0][1] * log(L[0][0])
line = 1
for i in range(len(L)):
    print i
    if L[i][1] * log(L[i][0]) > max_val:
        max_val = L[i][1] * log(L[i][0])
        line = i+1

print
print line, max_val
