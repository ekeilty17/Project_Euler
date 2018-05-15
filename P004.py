def isPalindrom(n):
    s_n = str(n)

    reverse_n = ""
    for i in range(len(s_n)-1,-1,-1):
        reverse_n += s_n[i]
    
    if s_n == reverse_n:
        return True
    else:
        return False

a = 100
b = 100
palindroms = []
while a < 1000:
    if isPalindrom(a*b):
        print a,b,a*b
        palindroms += [a*b]
    if b >= 1000:
        a += 1
        b = a
    else:
        b += 1

#bubble sort
for i in range(0,len(palindroms)-1):
    for j in range(0,len(palindroms)-1-i):
        if palindroms[j+1] < palindroms[j]:
            temp = palindroms[j]
            palindroms[j] = palindroms[j+1]
            palindroms[j+1] = temp

print palindroms
print palindroms[len(palindroms)-1]
