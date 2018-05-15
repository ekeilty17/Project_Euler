"""
a = 1
all_divide = False
while all_divide == False:
    a += 1
    print a
    all_divide = True
    for i in range(1,21):
        if a % i != 0:
            all_divide = False
"""
#the above brute forces it, but it would take way to long to find, so we can improve


a = 0
all_divide = False
while all_divide == False:
    #we increment by the product of all the numbers that share no common factors
    a += 20*19*17*13*11*7*3
    print a
    all_divide = True
    for i in range(1,21):
        if a % i != 0:
            all_divide = False

print a
