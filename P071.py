import math

def gcd(a, b):
    if b > a:
        return gcd(b, a)
    if b == 0:
        return 0
    if a % b == 0:
        return b
    return gcd(b, a%b)

def isLargerFraction(f1, f2):
    a, b = f1
    c, d = f2
    return a*d > c*b

# n = numerator
# d = denominator
def approximate_and_search(N, n, d):
    nearest_n, nearest_d = 0, 1

    # let a/b be the fraction we are considering
    for b in range(1, N+1):
        # we skip this case because otherwise we'd return a, b = n, d which we don't want
        if b == d:
            continue
        
        # The key idea is that we can approximate the numerator for a given denominator
        # and once we have this lower-bound, we can just iterate until we find the closest numerator without going over
        lower = math.floor( n/d * b )
        for a in range(lower, b+1):
            
            # if we are larger target fraction n/d, then we stop
            if isLargerFraction( (a, b), (n, d) ):
                
                # and we know that the previous fraction must be less than the target fraction n/d
                # therefore, we check (a-1)/b
                if gcd(a-1, b) == 1:
                    #print(f"{a-1}/{b} =", (a-1)/b)
                    if isLargerFraction( (a-1, b), (nearest_n, nearest_d) ):
                        nearest_n, nearest_d = a-1, b
                break
            
    return nearest_n, nearest_d

def main(N=10**6, numerator=3, denominator=7):
    nearest_frac = approximate_and_search(N, numerator, denominator)
    
    nearest_numerator, nearest_denominator = nearest_frac
    #print(f"\n{nearest_numerator}/{nearest_denominator} = {nearest_numerator / nearest_denominator}")
    print(f"The numerator of the reduced propert fraction immediately to the left of {numerator}/{denominator} with d <= {N} is:", nearest_numerator)
    return nearest_numerator

if __name__ == "__main__":
    main()