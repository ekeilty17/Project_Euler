def sqrt(n, digits=100):
    
    # putting n in a more usable form
    n = [int(x) for x in str(n)]
    if len(n) % 2 == 1:
        n = [0] + n
    
    c = 0
    y = 0
    p = 0
    while len(str(p)) < digits:
        
        # moving next two digits down
        c = 100*c + 10*n[0] + n[1]

        # adding zeros to end of number
        n = n[2:] + [0, 0]
        
        
        # finding x s.t. x(20p + x) <= c
        x = 0
        while x*(20*p + x) <= c:
            x += 1
        x -= 1
        
        # x is what goes on top as the next digit
        p = 10*p + x
        
        # y is what goes under the number that was brought down
        y = x*(20*p + x)
        # take the difference
        c -= y

    return p

def digital_sum(n):
    out = 0
    while n != 0:
        out += n%10
        n /= 10
    return out

print digital_sum(sqrt(2))

accum = 0
squares = [x**2 for x in range(1, 11)]
for n in range(1, 101):
    print n
    if n in squares:
        continue
    accum += digital_sum(sqrt(n))
print accum
