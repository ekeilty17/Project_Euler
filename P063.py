def is_d_digit_number(N, d):
    return 10**(d-1) <= N < 10**d

def numDigits(N):
    return len(str(N))

# The tricky part of this problem is to know when to stop searching
# we are looking at numbers of the form b^n
#
# What is an upper bound for the base, b
#   Notice that 10^n will always have n+1 digits
#   Thus, b^n will have >n digits for all b >= 10
#   Therefore, 1 <= b <= 9
#
# Now, for each given base, b, we can need a condition for which we can stop searching the exponent
#   we can notice that since the base is less than 10, by incrememting the exponent, we can at most increase the number of digits by 1
#   therefore, once the number of digits is strictly less than the exponent, it can never catch by
def brute_force():

    powerful_digits = []
    for b in range(1, 10):
        
        n = 1
        N = b**n
        while numDigits(N) >= n:
            print(b, n, numDigits(N), N)
            if numDigits(N) == n:
                powerful_digits.append( (b, n) )
            
            n += 1
            N = b**n

    return len(powerful_digits)

def main():

    total = brute_force()
    print(f"The number of n-digit positive integers that are also an nth power is:", total)
    return total

if __name__ == "__main__":
    main()