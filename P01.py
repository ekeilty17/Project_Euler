multiples = []
for i in range(0,1000):
    if i % 3 == 0 or i % 5 == 0:
        multiples += [i]

accum = 0
for i in range(0,len(multiples)):
    accum += multiples[i]

print multiples
print
print accum
