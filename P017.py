def ones(n):
    if n == 0:
        return 0
    elif n == 1:
        return 3 #one
    elif n == 2:
        return 3 #two
    elif n == 3:
        return 5 #three
    elif n == 4:
        return 4 #four
    elif n == 5:
        return 4 #five
    elif n == 6:
        return 3 #six
    elif n == 7:
        return 5 #seven
    elif n == 8:
        return 5 #eight
    elif n == 9:
        return 4 #nine
    else:
        return 0

def teens(n):
    if n < 10:
        return ones(n)
    elif n == 10:
        return 3 #ten
    elif n == 11:
        return 6 #eleven
    elif n == 12:
        return 6 #twelve
    elif n == 13:
        return 8 #thirteen
    elif n == 14:
        return 8 #fourteen
    elif n == 15:
        return 7 #fifteen
    elif n == 16:
        return 7 #sixteen
    elif n == 17:
        return 9 #seventeen
    elif n == 18:
        return 8 #eighteen
    elif n == 19:
        return 8 #nineteen
    else:
        return 0

def tens(n):
    if n == 0:
        return 0 #zero
    elif n == 10:
        return 3 #ten
    elif n == 20:
        return 6 #twenty
    elif n == 30:
        return 6 #thirty
    elif n == 40:
        return 5 #forty
    elif n == 50:
        return 5 #fifty
    elif n == 60:
        return 5 #sixty
    elif n == 70:
        return 7 #seventy
    elif n == 80:
        return 6 #eighty
    elif n == 90:
        return 6 #ninety
    else:
        return 0

def hundreds(n):
    if n % 100 != 0 or n == 0:
        return 0
    n /= 100
    return ones(n) + 7 #hundred

def thousands(n):
    if n % 1000 != 0 or n == 0:
        return 0
    n /= 1000
    return ones(n) + 8 #thousand

def Letters(n):
    count = 0
    if n >= 10000:
        return 0
    if n == 0:
        return 4 #zero
    if n < 0:
        n *= 1
        count += 8 #negative
    if n < 20:
        return count + teens(n)
    #splitting up n into its digits
    digits = []
    digits += [(n/1000)*1000]
    n = n % 1000
    digits += [(n/100)*100]
    n = n % 100
    digits += [n]
    
    count += thousands(digits[0])
    count += hundreds(digits[1])
    if digits[2] < 20:
        count += teens(digits[2])
    else:
        digits[2] = (n/10)*10
        n = n % 10
        digits += [n]
        count += tens(digits[2])
        count += ones(digits[3])

    if (digits[0] != 0 or digits[1] != 0) and (digits[2] != 0):
        count += 3 #and
    
    return count

accum = 0
for i in range(1,1001):
    print i
    accum += Letters(i)
print accum
