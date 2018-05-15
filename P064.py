"""
def ContinuedFraction(n):
    if n**0.5 == int(n**0.5):
        return (int(n**0.5),[0])
    #we iterate on the form (sqrt(n) + a)/b
    #   fract = [a, b]
    
    fract_prev = []
    fract = [0, 1]
    #print fract
    
    out = []
    while True:
        #so the logic of this is kinda annoying
        #the long out[...] stuff is just checking if the first half equals the second half
        #the out[1:] != [] is to account when out = [] at the beginning
        #after that we need to distinguish between sqrt(2) and sqrt(7)
        #   sqrt(2) leads to repeating 2's that repeat forever
        #   sqrt(7) leads to repeating 1's but eventually terminate at a 4
        #   the difference between these two is the fract list
        if out[1:len(out)//2+1] == out[len(out)//2+1:len(out)] and out[1:] != []:
            if out[-1] == out[-2]:
                if fract_prev == fract:
                    break
            else:
                break
        y = int((n**0.5 + fract[0])/fract[1])
        #print (n**0.5 + fract[0])/fract[1], '-->',y
        out += [y]
        fract_prev = list(fract)
        a = fract[0]
        b = fract[1]
        fract[0] = -a + b*y
        fract[1] = (n - (a-b*y)**2)/b
        #print fract
        #print
    return (out[0], out[1:len(out)//2+1])
"""
#the answer is off by two and I cannot for the life of me figure out why :(

#I still don't know why the above code is wrong, but it obviously fails in 2 cases
#The code below has much more straight forward logic and is correct
def ContinuedFraction(n):
    if n**0.5 == int(n**0.5):
        return (int(n**0.5),[0])
    #we iterate on the form (sqrt(n) + a)/b
    #   fract = [a, b]
    
    #sqrt(n) = (sqrt(n) + 0)/1
    fract = [0, 1]
    
    #(sqrt(n) + a)/b = y + 1/[ (sqrt(n) -a + b*y)/ ((n - (a-b*y)**2)/b) ]
    out = []
    while True:
        #If b ever equals 1, by definition we have reach the recurrive point
        if fract[1] == 1 and out != []:
            break
        y = int((n**0.5 + fract[0])/fract[1])
        out += [y]
        fract_prev = list(fract)
        a = fract[0]
        b = fract[1]
        fract[0] = -a + b*y
        fract[1] = (n - (a-b*y)**2)/b
    return (out[0], out[1:] + [fract[0] + int(n**0.5)])

cnt = 0
for i in range(2,10001):
    F = ContinuedFraction(i)
    print i,F
    if len(F[1])%2 == 1 and F[1] != [0]:
    #if len(F[1])%2 == 1:
        cnt += 1

print cnt
