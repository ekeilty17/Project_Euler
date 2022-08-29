def decimal_to_binary(n):
    if n == 0:
        return 0
    return n%2 + 10*decimal_to_binary(n//2)

def getDigits(n):
    return [int(d) for d in str(n)]

def isPalindrome(n):
    d = getDigits(n)
    if len(d)%2 == 0:
        if d[0:len(d)//2] == list(reversed(d[len(d)//2:])):
            return True
    else:
        if d[0:len(d)//2] == list(reversed(d[len(d)//2+1:])):
            return True
    return False

# This is pretty fast, but could be faster
# Not sure if there's some other method to improve it
def main(N=10**6):

    total = 0
    for i in range(N):
        if isPalindrome(i) and isPalindrome(decimal_to_binary(i)):
            total += i
    
    print(f"The sum of all numbers, less than {N}, which are palindromic in base 10 and base 2 is:", total)
    return total

if __name__ == "__main__":
    main()