def digit_cancelling_fractions():
    fracts = set()
    denominator = 2
    while len(fracts) < 4:
        for numerator in range(1, denominator):
            for x in range(1, 10):
                for i in range(len(str(numerator))+1):
                    for j in range(len(str(denominator))+1):
                        n = int(str(numerator)[:i] + str(x) + str(numerator)[i:])
                        d = int(str(denominator)[:j] + str(x) + str(denominator)[j:])
                        if numerator/denominator == n/d:
                            fracts.add((n, d))
        denominator += 1
    return fracts

# finding GCF using Euliers Method
def gcd(a,b):
    if b > a:
        return gcd(b, a)
    if a % b == 0:
        return b
    return gcd(b, a%b)

def main():
    
    fractions = digit_cancelling_fractions()
    #print(fractions)

    # multiplying them 
    numerator = denominator = 1
    for n, d in fractions:
        numerator   *= n
        denominator *= d
    
    # Simplifying to lowest terms
    divisor = gcd(numerator, denominator)
    numerator   = numerator   // divisor
    denominator = denominator // divisor

    print(f"The denominator of the product of all digit cancelling fractions less than 1 in lowest terms is:", denominator)
    return denominator

if __name__ == "__main__":
    main()