accum = 0
for i in range(1,1000):
    accum += (i**i) % (10**10)

print accum % 10**10
