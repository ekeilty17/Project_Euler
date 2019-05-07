
prime = 28433
d = 10**10
for i in range(7830457):
    print i, prime
    prime *= 2
    prime %= d

prime += 1

print prime
