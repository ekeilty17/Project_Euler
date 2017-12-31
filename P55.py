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

def Lychrel(n):
    x = n
    counter = 0
    while isPalindrome(x) == False and counter < 53:
        print str(x) + " + " + str(reverse(x)) + " = " + str(x + reverse(x))
        x += reverse(x)
        counter += 1
    return isPalindrome(x)

counter = 0
for i in range(1,10001):
    if Lychrel(i):
        counter += 1

print "number of Lechrel numbers under 10,000 is",counter
