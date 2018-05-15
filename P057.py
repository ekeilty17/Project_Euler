n = 8
#representing the fraction a/b using [a,b]
fract = [2,1]
cnt = 0
for i in range(0,1000):
    #making out
    out = [fract[1], fract[0]]
    out[0] += out[1]

    #take the recipricle
    temp = fract[1]
    fract[1] = fract[0]
    fract[0] = temp
    #add 2 to it
    fract[0] += 2*fract[1]
    
    if len(str(out[0])) > len(str(out[1])):
        cnt += 1
    print out[0],out[1]

#print "number of times the number of digits in the numerator exceed the number to digits in the denominator:",cnt
print
print cnt
