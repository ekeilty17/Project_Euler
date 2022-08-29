import math

def herons_formula(a, b, c):
    s = (a + b + c)/2
    return math.sqrt(s * (s-a) * (s-b) * (s-c))

def herons_formula_squared(a, b, c):
    s = (a + b + c)/2
    return s * (s-a) * (s-b) * (s-c)

def isPerfectSquare(n):
    s = math.sqrt(n)
    return math.floor(s)**2 == n or math.floor(s)**2 == n

# While this should work in theory
# because the areas get so large, checking if they are perfect squares is numerically unstable
# Also takes way too long
def brute_force(N):

    almost_equilateral_triangles = []

    total = 0
    # Note that a=1 doesn't form a triangle in either case
    # (1, 1, 0) is not a triangle and (1, 1, 2) is not a triangle
    for a in range(2, N//3+1):
        #print(a)
        A1_sqaured = herons_formula_squared(a, a, a-1)
        if isPerfectSquare(A1_sqaured):
            P = 3*a - 1
            if P <= N:
                almost_equilateral_triangles.append((a, a, a-1))
                total += P

        A2_sqaured = herons_formula_squared(a, a, a+1)
        if isPerfectSquare(A2_sqaured):
            P = 3*a + 1
            if P <= N:
                almost_equilateral_triangles.append((a, a, a+1))
                total += P

    #print(almost_equilateral_triangles)
    return total


# we can do some math and show that herons formula for the area of an almost-perfect triangle is the following
#   (a, a, a-1) --> Area = (a-1)/4 * sqrt(3a^2 + 2a - 1)
#   (a, a, a+1) --> Area = (a+1)/4 * sqrt(3a^2 - 2a - 1)
# Gives the correct answer, but still takes way too long
def brute_force_numerically_stable(N):

    almost_equilateral_triangles = []

    total = 0
    # Note that a=1 doesn't form a triangle in either case
    # (1, 1, 0) is not a triangle and (1, 1, 2) is not a triangle
    for a in range(2, N//3+1):
        print(a)
        n1_sqaured = 3*a**2 + 2*a - 1
        if isPerfectSquare(n1_sqaured):
            n1 = int(math.sqrt(n1_sqaured))
            if (((a-1) % 4) * (n1 % 4)) % 4 == 0:
                P = 3*a - 1
                if P <= N:
                    almost_equilateral_triangles.append((a, a, a-1))
                    total += P
        
        n2_sqaured = 3*a**2 - 2*a - 1
        if isPerfectSquare(n2_sqaured):
            n2 = int(math.sqrt(n2_sqaured))
            if (((a+1) % 4) * (n2 % 4)) % 4 == 0:
                P = 3*a + 1
                if P <= N:
                    almost_equilateral_triangles.append((a, a, a+1))
                    total += P

    print(almost_equilateral_triangles)
    return total

# Our goal is to find when sqrt(3a^2 +/- 2a - 1) is an integer
# Doing some algebra, we can show that 
#       3a^2 +/- 2a - 1 = 3(a -/+ 1/3)^2 - 4/3
#
# now, we want to find values of a that make this expression a perfect square, i.e.
#       3(a -/+ 1/3)^2 - 4/3 = k^2
# 
# Let X = 3a +/- 1 and Y = k, the above can be re-written as 
#       X^2 - 4 = 3Y^2      -->     X^2 - 3Y^2 = 4 
# 
# Recall the form of the Pell Equation:                     x^2 - d y^2 = 1
# The above is a form of the Generalized Pell Equation:     X^2 - d Y^2 = N
# However, the case where N=4 is a special case
# Let X = 2x and Y = 2y
#       X^2 - d Y^2 = 4     -->     (2x)^2 - d (2y)^2 = 4   -->     x^2 - d y^2 = 1
#
# Therefore, we can get the solutions to the N+4 case from the fundamental solutions to the regular Pell equation
#
# In the case of d=3, the fundamental solution to the pell equation is (x, y) = (2, 1)
#
# Now, x_n + sqrt(3) * y_n = (2 + 1 * sqrt(3))^n will give all solutions to our pell equation
# All solutions to this pell equation tell us when we have an integer area
# we can back calculate the side length a and check that it's an integer, and if it is, then we have a solution

def multiply_pell_solutions(S1, S2, d):
    x1, y1 = S1
    x2, y2 = S2
    return (x1*x2 + d * y1*y2), (x1*y2 + x2*y1)


def pell_equation_method(N):
    # initialize our solutions to the pell equation
    x0, y0 = 2, 1
    xn, yn = x0, y0         # nth solutions to      x^2 - d * y^2 = 1
    X, Y = 2*xn, 2*yn       # nth solutions to      x^2 - d * y^2 = 4

    almost_equilateral_triangles = []
    total = 0
    while X <= N:           # X is the perimeter

        # update pell equation solutions
        xn, yn = multiply_pell_solutions((xn, yn), (x0, y0), d=3)
        X, Y = 2*xn, 2*yn
        

        # Note: The area of the almost equilateral triangle is now
        #       (a +/- 1)/4 * Y
        # You can actually prove that this will always be an integer
        #
        # Notice that since Y = 2 * yn      -->     Y is always divisible by 2
        #
        # Also notice that X = 2 * xn       -->     a = (2xn +/- 1)/3, which is always odd
        # Therefore, (a +/- 1) is divisible by 2
        #
        # Therefore,    (a +/- 1) * Y     is divisible by 4
        # so we do not have to check that the area is an integer, it follows from this method
        

        # from the above derivation, X = 3a +/- 1
        # Amazingly, this is precicely the perimeter of the almost equilateral triangle
        P = X

        # We have two cases for almost equilateral triangles
        #   (a, a, a-1) and (a, a, a+1)
        
        # In the case of (a, a, a-1), P = 3a-1
        # therefore, a is an integer if (P-1)%3 == 0    -->     P%3 = 1 
        if P % 3 == 1:
            a = (P-1)//3
            if P <= N:
                almost_equilateral_triangles.append((a, a, a-1))
                total += P
    
        # In the case of (a, a, a+1), P = 3a+1
        # therefore, a is an integer if (P+1)%3 == 0    -->     P%3 = 2 
        elif P % 3 == 2:
            a = (P+1)//3
            if P <= N:
                almost_equilateral_triangles.append((a, a, a+1))
                total += P
        
        else:
            # X being divisible by 3 is impossible since d=3
            print("This should never happen")

    #print(almost_equilateral_triangles)
    return total

def main(N=10**9):
    #total = brute_force(N)
    #total = brute_force_numerically_stable(N)
    total = pell_equation_method(N)

    print(f"The sum of the perimeters of all almost equilateral triangles with integral side lengths and area and whose perimeters do not exceed {N} is:", total)
    return total

if __name__ == "__main__":
    main()