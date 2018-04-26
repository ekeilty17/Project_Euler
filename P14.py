def Collatz(n):
    count = 1
    out = ""
    while n != 1:
        out += str(n) + " -> "
        if n % 2 == 0:
            n /= 2
        else:
            n = 3*n + 1
        count += 1
    out += "1"
    #print out
    return count

max_chain = 0
max_chain_num = 1
for i in range(1, 1000001):
    C = Collatz(i)
    print i,C
    if C > max_chain:
        max_chain = C
        max_chain_num = i

print
print max_chain_num,max_chain
