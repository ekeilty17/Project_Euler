import math

#stealing my code from P7
def isPrime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n == 3:
        return True
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def nthPrime(n):
    if n < 1:
        return 1

    counter = 0
    candidate = 1
    while counter < n:
        candidate += 1
        if isPrime(candidate):
            counter += 1
    return candidate

#also I need a function that concatinates numbers
def concat(a,b):
    s_a = str(a)
    s_b = str(b)
    out = s_a+s_b
    return int(out)
"""
#Let's try to find a number by just adding it to the original list
#original list: 3, 7, 109, 673

#you know right away it can't be 2, 3, 5, or 7 just from the original list
candidate = 7 #this is the 4th prime
n = 4

all_prime = False
while all_prime == False and candidate < 1000:
    
    candidate = nthPrime(n+1)
    n += 1
    
    #make a list of every concatination
    concat_list = [ concat(3,candidate), concat(candidate,3),
                    concat(7,candidate), concat(candidate,7),
                    concat(109,candidate), concat(candidate,109),
                    concat(673,candidate), concat(candidate,673)
                  ]

    for c in concat_list:
        all_prime = True
        if isPrime(c) == False:
            all_prime = False
            break

print "next prime in the set is",candidate
accum = 3+7+109+673+candidate
print "lowest sum in the set",accum
#turns out this isn't the lowest sum
"""

a = 13
b = 13
c = 13
d = 13
e = 13

p_set = [a,b,c,d,e]

n_a = 6
n_b = 6
n_c = 6
n_d = 6
n_e = 6

n_set = [n_a,n_b,n_c,n_d,n_e]

for i in range(0,len(p_set)-1):
    all_prime = False
    while all_prime == False and p_set[i+1] < 10000:
        
        for j in range(i+1,len(p_set)):
            p_set[j] = nthPrime(n_set[j]+1)
            n_set[j] += 1
    
        #make a list of every concatination
        concat_list = []
        for j in range(0,len(p_set)-1):
            concat_list += [ concat(p_set[j],p_set[j+1]) ]
            concat_list += [ concat(p_set[j+1],p_set[j]) ]

        for p in concat_list:
            all_prime = True
            if isPrime(p) == False:
                all_prime = False
                break

print p_set
