#int combos

L = []
for a in range(2,101):
    for b in range(2,101):
        if a**b not in L:
            L += [a**b]

print len(L)
