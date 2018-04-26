def isLeapYear(y):
    if y % 4 == 0:
        if y % 100 == 0:
            if y % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
  
def dayFromDate(dd, mm, yyyy):
    days = {
        "Monday": 0, 
        "Tuesday": 1, 
        "Wednesday": 2, 
        "Thurseday": 3, 
        "Friday": 4,
        "Saturday": 5, 
        "Sunday": 6
    }
    #         Jan, Feb, Mar, Apr, May, June, July, Aug, Sept, Oct, Nov, Dec
    Months = [31,  28,  31,  30,  31,  30,   31,   31,  30,   31,  30,  31]
  
    Jan1_1900 = 0
    Jan1_yyyy = 0
    for i in range(1900, yyyy):
        if isLeapYear(i):
            Jan1_yyyy += 366
        else:
            Jan1_yyyy += 365
  
    num_days = 0
    for i in range(0, mm-1):
        num_days += Months[i]
    if isLeapYear(yyyy) and mm > 2:
        num_days += 1
    num_days += dd - 1
    return (Jan1_yyyy + num_days) % 7

accum = 0
for y in range(1901,2001):
    for m in range(1,13):
        print 1,m,y
        if dayFromDate(1,m,y) == 6:
            accum += 1

print accum
