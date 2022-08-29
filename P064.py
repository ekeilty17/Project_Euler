import math

def SquareRootContinuedFraction(n):
    # This computes the continued fraction of a square root function

    # if n is a perfect square
    if math.sqrt(n) == int(math.sqrt(n)):
        return [ int(math.sqrt(n)) ]
    
    # we iterate on the form (sqrt(n) + a)/b
    # to get to the next iteration, we need to rewrite the above as
    #       y + 1/( (sqrt(n) + a')/b' )
    # where y = floor( sqrt(n) )       i.e. it's the non-decimal part
    #
    # Doing some math, we can show that 
    #       a' = by - a
    #       b' = (n - (by-a)^2)/b = (n - (a')^2)/b

    
    # sqrt(n) = (sqrt(n) + 0)/1
    a, b = 0, 1
    continued_fraction = []

    # If b ever equals 1, by definition we have reach the recurrive point
    # because we'll have something of the form sqrt(n) + a
    # and after the next iteration, everything will just repeat
    while b != 1 or len(continued_fraction) == 0:
        
        y = math.floor( (math.sqrt(n) + a)/b )
        continued_fraction.append(y)
        a = b*y - a
        b = (n - a**2) // b
    
    # we just need to add the last iteration to complete the cycle
    y = math.floor( (math.sqrt(n) + a)/b )
    continued_fraction.append(y)
    return continued_fraction

def main(N=10**4):
    
    odd_periods = []
    for n in range(2, N+1):
        continued_fraction = SquareRootContinuedFraction(n)
        first_digit, period = continued_fraction[0], continued_fraction[1:]
        #print(n, [first_digit, tuple(period)])
        if len(period) % 2 == 1:
            odd_periods.append(n)

    total = len(odd_periods)
    print(f"The number of continued fractions for numbers <= {N} that have an odd period is:", total)
    return total

if __name__ == "__main__":
    main()