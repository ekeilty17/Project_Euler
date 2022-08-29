def factorial(n):
    if n <= 0:
        return 1
    return n*factorial(n-1)

def getDigits(n):
    return [int(d) for d in str(n)]

# The hard part of this problem is to know when you can stop searching
# Observe:
# 9       < 1*9! = 362880
# 99      < 2*9! = 725760
# 999     < 3*9! = 1088640
# 9999    < 4*9! = 1451520
# 99999   < 5*9! = 1814400
# 999999  < 6*9! = 2177280
# 9999999 > 7*9! = 2540160

# So we don't have to search past 10**7
# because the factorial sum will always be smaller than the number itself

def search():
    f = []
    factorials = [factorial(n) for n in range(10)]  # pre-compute these so it's faster

    # don't include 1! and 2!
    for n in range(3, 10**7):
        total = sum([factorials[int(d)] for d in str(n)])
        if total == n:
            f.append(n)
    return f

# TODO: This search is relatively quick (takes about 10 seconds), but it can definitely be faster
# Either there is some trick to prune the higher numbers, or we can get a better upper bound for the search

def main():
    
    f = search()
    print(f)
    print(f"The sum of all numbers which are equal to the sum of the factorial of their digits is:", sum(f))
    return sum(f)

if __name__ == "__main__":
    main()