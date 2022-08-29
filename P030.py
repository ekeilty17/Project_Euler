def digit_power_sum(n, e):
    return sum([int(d)**e for d in str(n)])

# That hard part about this problem is knowing how far to look in your search
# Take N=4 for example
#   9     < 1 * 9^4 = 6561
#   99    < 2 * 9^4 = 13122
#   999   < 3 * 9^4 = 19683
#   9999  < 4 * 9^4 = 26244
#   99999 > 5 * 9^4 = 32805
# So we know, we don't have to check anything beyond 10^5-1
# because it will always be larger than the 4th-power sum of its digits

def upper_bound(e):
    d = 1
    while (10**d)-1 < d * (9**e):
        d += 1
    return 10**d

def main(N=5):
    
    U = upper_bound(N)
    powers_sums = [n for n in range(2, U) if n == digit_power_sum(n, N)]
    total = sum(powers_sums)
    
    #print(powers_sums)
    print(f"The sum of all the numbers that can be written as the sum of powers of {N} of their digits is:", total)
    return total

if __name__ == "__main__":
    main()