def numDigits(n):
    return len([int(d) for d in str(n)])

def gcd(a, b):
    if b > a:
        return gcd(b, a)
    if a % b == 0:
        return b
    return gcd(b, a%b)

def reduce_fraction(numerator, denominator):
    k = gcd(numerator, denominator)
    return numerator // k, denominator // k

def partial_continued_fractions(N):
    
    # representing the fraction as a/b, we start at 1
    a = 1
    b = 1
    
    cnt = 0
    for _ in range(0, N):
        # n <-- 1 + 1/(1 + n)
        # Thus if n = a/b, then a/b <-- 1 + 1/(1 + a/b) = 1 + 1/((b+a)/b) = 1 + b/(a+b) = (a+2b)/(a+b)
        a, b = a+2*b, a+b
        
        if numDigits(a) > numDigits(b):
            cnt += 1

    return cnt


def main(N=1000):
    
    total = partial_continued_fractions(N)
    print(f"The number of partial continued fractions of sqrt(2) in the first {N} expansions that contain a numerator with more digits than the denominator is:", total)
    return total

if __name__ == "__main__":
    main()
