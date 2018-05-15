def DigitSum(n):
    accum = 0
    while n != 0:
        accum += n%10
        n /= 10
    return accum

mx_sum = 0
num = [0,0]

for a in range(1,100):
    for b in range(1,100):
        s = DigitSum(a**b)
        if s > mx_sum:
            mx_sum = s
            num = [a,b]

print mx_sum
print num
print num[0]**num[1]
