s = str(2**1000)

a = []
for i in range(0,len(s)):
    a += [int(s[i])]

print sum(a)
