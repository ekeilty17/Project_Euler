import math

def num_digits(n):
    return int(math.floor(math.log10(n)))+1   

d = 1000
cnt = 2
prev = [1, 1]
while num_digits(prev[1]) < d:
    temp = prev[1]
    prev[1] += prev[0]
    prev[0] = temp
    cnt += 1

print prev, cnt
