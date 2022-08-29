import math
import numpy as np

def isPerfectSquare(n):
    s = math.sqrt(n)
    return math.floor(s)**2 == n or math.floor(s)**2 == n

# The brute force method takes about 5 minutes, which isn't too bad
# but we can do much better using some results from number theory
def brute_force(D, limit=10**10):
    # perfect squares have no solution
    if isPerfectSquare(D):
        return 0
    
    y = 1
    while y < limit:
        # If we find a perfect square, we can stop because (1 + D*y^2) always increases
        if isPerfectSquare(1 + D*y*y):
            return int(math.sqrt(1 + D*y*y))
        
        y += 1
    
    # couldn't find a solution under the limit
    return 0


# using a paper by Hendrik W. Lenstra, Jr. http://library.msri.org/books/Book44/files/01lenstra.pdf
# We notice that we can factor 
#       x^2 - d y^2 = 1     -->     (x + y * sqrt(d)) * (x - y * sqrt(d)) = 1
# 
# Now we can view all numbers of the form (x + y * sqrt(d)) as a ring 
# with (x + y * sqrt(d)) * (x - y * sqrt(d)) defined as the norm of (x + y * sqrt(d))
# as a short-hand, I'll write (x + y * sqrt(d)) as a vector [x, y]
# 
# Notice that if we find |[x, y]| = 1, then |[x, y]|^n = 1
# So there are an infinite number of solutions to x^2 - d y^2 = 1, but the smallest such solution is called the fundamental solution
# 
# Recall the periodicity of the partial fractions of sqaure roots
# take d = 14 as an example,
#   the sqrt(14) can be written as the repeated fraction: [3, (1, 2, 1, 6)]
#
# # We apply Dirichlet’s unit theorem from algebraic number theory
#   If we truncate that at the last element in the period you get [3, (1, 2, 1)]
#   evaluating that continued fraction gives 15/4, which is a good approximation to sqrt(14)
#   Notice 15**2 - 14*(4**2) = 1
#
# For a general d, we use results from Buhler and Wagon 2008
#   If the period of sqrt(d) is even, then we truncate at the end of the first period
#   If the period of sqrt(d) is odd, then we truncate at the end of the second period


# code from P064.py
def SquareRootContinuedFraction(n):
    if math.sqrt(n) == int(math.sqrt(n)):
        return [ int(math.sqrt(n)) ]

    a, b = 0, 1
    continued_fraction = []

    while b != 1 or len(continued_fraction) == 0:
        
        y = math.floor( (math.sqrt(n) + a)/b )
        continued_fraction.append(y)
        a = b*y - a
        b = (n - a**2) // b
    
    y = math.floor( (math.sqrt(n) + a)/b )
    continued_fraction.append(y)
    return continued_fraction


def gcd(a, b):
    if b > a:
        return gcd(b, a)
    if a % b == 0:
        return b
    return gcd(b, a%b)

# code from P065.py
def calculateTruncatedFraction(continued_fraction):
    
    a, b = 1, 0
    for n in reversed(continued_fraction):
        a, b = a*n + b, a
    
    # You don't actually need to do this because it everything will always be relatively prime
    #g = gcd(a, b)
    #a = a // g
    #b = b // g
    return a, b

def pell_equation(D):
    # perfect squares have no solution
    if isPerfectSquare(D):
        return 0
    
    # continued fraction of sqrt(D)
    continued_fraction = SquareRootContinuedFraction(D)

    if len(continued_fraction) % 2 == 1:
        continued_fraction = continued_fraction[:-1]        # if length of the period is odd, we do one cycle
    else:
        continued_fraction += continued_fraction[1:-1]      # if length of the period is even, we do two cycles

    # According to Dirichlet’s unit theorem, these will be the fundamental solutions
    x, y = calculateTruncatedFraction(continued_fraction)
    return x

def main(N=1000):

    X = [0, 0]      # X[D] is the minimum value x that satisfy the Diophantine equation with D, 0 means no solution
    for D in range(2, N+1):
        #x = brute_force(D)
        x = pell_equation(D)
        #print(D, x)
        X.append(x)
    
    D_max = np.argmax(X)
    x_max = max(X)
    #print(x_max)
    print(f"The value of D <= {N} in minimal solutions of x for which the largest value of x is obtained is:", D_max)
    return D_max

if __name__ == "__main__":
    main()
