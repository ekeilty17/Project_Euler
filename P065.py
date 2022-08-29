def sumDigits(n):
    return sum([int(d) for d in str(n)])

def gcd(a, b):
    if b > a:
        return gcd(b, a)
    if a % b == 0:
        return b
    return gcd(b, a%b)

def eContinuedFraction(n):
    continued_fraction = [2]
    for k in range(1, (n//3)+2):
        continued_fraction += [1, 2*k, 1]
    
    extra = 3 - (n%3)
    continued_fraction = continued_fraction[:-extra-1]

    return continued_fraction

def calculateTruncatedFraction(continued_fraction):

    # let the fraction be represented by a/b
    # when we iterate to the next fraction, we will have
    #   n + 1/(a/b) = (an + b)/a
    # Therefore,
    #   a' = an + b
    #   b' = a
    
    a, b = 1, 0
    for n in reversed(continued_fraction):
        a, b = a*n + b, a
    
    # you actually don't need this because they will always be relatively prime
    #g = gcd(a, b)
    #a = a // g
    #b = b // g

    return a, b

def main(N=100):

    e_continued_fraction = eContinuedFraction(N)
    numerator, denominator = calculateTruncatedFraction(e_continued_fraction)
    
    total = sumDigits(numerator)
    print(f"The sum of digits in the numerator of the {N} continued fraction for e is:", total)
    return total

if __name__ == "__main__":
    main()
