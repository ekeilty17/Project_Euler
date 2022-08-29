import math
import numpy as np

def Pentagon(n):
    return (n*(3*n-1)) // 2

# n * (3*n - 1) / 2 = x
# 3*n^2 - n = 2x
# n^2 - 1/3 * n = 2/3 * x
# (n - 1/6)^2 = 2/3 * x + 1/36
# n = 1/6 + sqrt(2/3 * x + 1/36)
# n = (1 + sqrt(24x + 1)) / 6

def isPentagon(x):
    n = (1 + math.sqrt(24*x + 1)) / 6
    return x == Pentagon(math.floor(n)) or x == Pentagon(math.ceil(n))


# So this will give the correct solution, and this is what yuo will see if you look up other people's solutions
# but it's not a correct algorithm I think it's just lucky that it is correct
# because it's entirely possible that there exists another pair with higher j, k indicies and a smaller difference
def naive_brute_force():
    
    k = 2
    while True:
        Pk = Pentagon(k)
        for j in range(1, k):
            Pj = Pentagon(j)
            #print(Pj, Pk, Pk - Pj)
            if isPentagon(Pk + Pj) and isPentagon(Pk - Pj):
                return Pj, Pk
        k += 1


# This is still pretty slow, but I think it's the only way to solve it correctly
# This is my least favorite Project Euler question so far
def correct_brute_force():

    min_Pk = min_Pj = None
    min_D = np.inf

    k = 2
    while True:

        Pk = Pentagon(k)
        # we use that fact that P_{n+1} - P_{n} > P_{n} - P_{n-1} for all n
        # so once we find a place where P_{k} - P_{k-1} > the found difference
        # then we know for sure that no other smallest difference exists
        if Pk - Pentagon(k-1) > min_D:
            break

        for j in reversed(range(1, k)):
            Pj = Pentagon(j)
            #print(Pj, Pk, Pk - Pj)
            # the differences are only getting larger since we iterate in reverse, 
            # so we can break once this condition is met
            if Pk - Pj > min_D:
                break
            
            # This is just the same as the previous algorithm
            if isPentagon(Pk + Pj) and isPentagon(Pk - Pj):
                if Pk - Pj < min_D:
                    min_D = Pk - Pj
                    min_Pj, min_Pk =  Pj, Pk
                    found = True
        k += 1

    return min_Pj, min_Pk

def main():

    #Pj, Pk = naive_brute_force()
    Pj, Pk = correct_brute_force()
    D = abs(Pk - Pj)
    print(f"The minimum difference between any pair of pentagonal numbers is:", D)
    return D

if __name__ == "__main__":
    main()