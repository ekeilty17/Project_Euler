import math

"""
You can reduce the problem to finding integer solutions to the equation
        2 * b(b - 1) = T(T - 1)
where b = number of blue disks and T = total number of disk

plotting this gives you a hyperbola, where the integer solutions to this equation 
lie on the ray going up and to the right. This ray can be approximated with the line
        T = sqrt(2) * (b - 0.5) + 0.5

Thus, this problem can be reduced to finding good rational approxations to the sqrt(2), i.e.
        T/b ~ sqrt(2)

The best way to find rational approxations to an irrational number is to use contionued fractions
I created this code in P065.py

At first it doesn't track with the solution because the best rational approxations aren't quite on the above line
But for very large T, b they are equivalent
"""

"""
# doesn't get you very far
def naive_search(Upper=1e12):

    T, b = 21, 15

    while T < Upper:
        prob = P_exact(T, b)
        if 2 * prob[0] == prob[1]:
            print(f"\tT={T} \t b={b} \t\t sqrt(2) = {T/b} \t\t P = {prob[0]}/{prob[1]} = {prob[0] / prob[1]}")
            T += 1

        if 2 * prob[0] < prob[1]:
            b += 1
        else:
            T += 1
"""

# way too slow, can barely get through each individual n
def brute_force_linear_search(N):

    n = N
    while True:
        print(n)
        total = n * (n-1)

        for b in range(1, n+1):
            if 2 * b * (b-1) == total:
                return b, n
            if b * (b-1) > total:
                break

        n += 1

# fast for each individual n, but is the wrong approach for this problem
def brute_force_binary_search(N):

    n = N
    while True:
        print(n)
        total = n * (n-1)
        
        b_low, b_high = 1, n
        
        while b_low + 1 < b_high:
            m = (b_low + b_high) // 2

            if 2 * m * (m-1) == total:
                return m, n
            
            if 2 * m * (m-1) < total:
                b_low = m
            else:
                b_high = m

        n += 1
    

# We can transform this problem into solving the pell equation in the following way
#   let b = the number of blue discs
#   let n = the total number of discs
#   
#   we wish to find when b/n * (b-1)/(n-1) = 1/2
#   or when 2b(b-1) = n(n-1)
#   
#   substitute in   n = (x+1)/2     and     b = (y+1)/2
#   we get the equation     x^2 - 2y^2 = -1
#
#   This is a pell equation with d=2
#   The fundamental solution is (x, y) = (1, 1)
#   So, we just have to find a solution to this pell equation with n > N

def multiply_pell_solutions(S1, S2, d):
    x1, y1 = S1
    x2, y2 = S2
    return (x1*x2 + d * y1*y2), (x1*y2 + x2*y1)

def pell_equation_method(N):
    # initialize our solutions to the pell equation
    x0, y0 = 1, 1
    xn, yn = x0, y0         # nth solutions to      x^2 - d * y^2 = -1

    n, b = (xn+1)//2, (yn+1)//2
    while n < N:
        # since this pell equation equals -1, we have to multiply the fundamental solution twice
        # because the intermediate will be the solution when the pell equation equals +1
        xn, yn = multiply_pell_solutions((xn, yn), (x0, y0), d=2)
        xn, yn = multiply_pell_solutions((xn, yn), (x0, y0), d=2)
        
        n, b = (xn+1)//2, (yn+1)//2
    
    return b, n

def main(N=10**12):

    #b, n = brute_force_linear_search(N)
    #b, n = brute_force_binary_search(N)
    b, n = pell_equation_method(N)

    print(f"The number of blue discs in first arrangement containing over {N} discs in total such that P(BB) = {0.5} is:", b)
    return b

if __name__ == "__main__":
    main()