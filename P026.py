#these two functions coupled together do division

#[a//b, a%b]
def remainder(a,b):
    if a < b:
        return [0, a]
    k = 0
    while k*b <= a:
        k += 1
    k -= 1
    return [k, a-k*b]

#a/b
def division(a,b,maximum=10):
    out = []
    r = remainder(a,b)
    out += [r[0]]
    out += ['.']
    a = r[1]

    cnt = 0
    while cnt < maximum:
        r = remainder(a*10,b)
        out += [r[0]]
        a = r[1]
        cnt += 1
    return out

def find_cycle(a,b,maximum=20):
    #get digits
    digits = division(a,b,maximum)
    digits = digits[2:]
    
    #since I'm checking for cycles in integeres under 1000
    #I need to look for repeats for 4
    for i in range(4,len(digits)):
        for j in range(0,len(digits)-i,i):
            if digits[0+j:i+j] == digits[i+j:2*i+j]:
                return i
    return None

max_cycle = 0
num = 0
for i in range(1,1000):
    f = find_cycle(1,i,10000)
    print i,f
    if f > max_cycle:
        max_cycle = f
        num = i
print num
