def reverse_int(n):
    return int( "".join(reversed(str(n))) )

def isPalindrome(n):
    return n == reverse_int(n)

def isLychrelNumber(n):

    # we need to do the above step once outside the loop 
    # bc a number can be a Palindrome, but still a Lychrel number
    iterations = 1
    n += reverse_int(n)
    
    while (not isPalindrome(n)) and iterations < 50:
        n += reverse_int(n)
        iterations += 1
    return not isPalindrome(n)

def main(N=10**4):
    
    lychrel_numbers = []
    for n in range(1, N):
        if isLychrelNumber(n):
            lychrel_numbers.append(n)
    #print(lychrel_numbers)

    print(f"The number of Lychrel numbers below {N} is:", len(lychrel_numbers))
    return len(lychrel_numbers)

if __name__ == "__main__":
    main()