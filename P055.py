#make a function outputs the reverse of a number
def reverse(n):
    s_n = str(n)
    rs_n = ""
    for i in range(len(s_n)-1,-1,-1):
        rs_n += s_n[i]
    return int(rs_n)

#make a function that checks if a number is a palindrone
def isPalindrome(n):
    if n == reverse(n):
        return True
    else:
        return False

def Lychrel(x):
    cnt = 0
    x += reverse(x) 
    #we need to do the above step once outside the loop 
    #bc there are cases where a number is a Palindrome, but still a Lychrel number
    while (not isPalindrome(x)) and cnt < 49:
        #print str(x) + " + " + str(reverse(x)) + " = " + str(x + reverse(x))
        x += reverse(x)
        cnt += 1
    return not isPalindrome(x)

cnt = 0
out = []
for i in range(1,10000):
    if Lychrel(i):
        print i
        out += [i]
        cnt += 1
    #print

print
print cnt
