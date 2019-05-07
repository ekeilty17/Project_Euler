# It's not very efficient, but it works

def square_digits(n):
    return sum([int(x)**2 for x in str(n)])

def Chain(n):
    out = [n]
    while n != 1 and n != 89:
        n = square_digits(n)
        out += [n]
    return out

N = 10 * 10**6
cnt = 0
for i in range(1, N):
    print i
    if Chain(i)[-1] == 89:
        cnt += 1

print
print cnt
