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
  
def day_from_date(dd, mm, yyyy):
    days = {
        "Monday": 0, 
        "Tuesday": 1, 
        "Wednesday": 2, 
        "Thurseday": 3, 
        "Friday": 4,
        "Saturday": 5, 
        "Sunday": 6
    }
    #                 Jan, Feb, Mar, Apr, May, June, July, Aug, Sept, Oct, Nov, Dec
    days_in_months = [31,  28,  31,  30,  31,  30,   31,   31,  30,   31,  30,  31]
  
    Jan1_1900 = 0
    Jan1_yyyy = 0
    for i in range(1900, yyyy):
        if isLeapYear(i):
            Jan1_yyyy += 366
        else:
            Jan1_yyyy += 365
  
    num_days = 0
    for i in range(0, mm-1):
        num_days += days_in_months[i]
    if isLeapYear(yyyy) and mm > 2:
        num_days += 1
    num_days += dd - 1
    return (Jan1_yyyy + num_days) % 7

def main():

    total = 0
    for yyyy in range(1901,2001):
        for mm in range(1,13):
            if day_from_date(1, mm, yyyy) == 6:       # 6 is Sunday
                total += 1

    print(f"The number of Sundays that fell on the first of the month during the twentieth century is:", total)
    return total

if __name__ == "__main__":
    main()