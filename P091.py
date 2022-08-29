from itertools import product
import math

def distance_squared(C1, C2):
    x1, y1 = C1
    x2, y2 = C2
    return (x2-x1)**2 + (y2-y1)**2

def isRightTriangle(C1, C2, C3):
    S = list(sorted([distance_squared(C1, C2), distance_squared(C2, C3), distance_squared(C3, C1)]))
    return (S[0] + S[1]) == S[2]


def brute_force(N):
    # We get all coordinates in the grid
    coordinates = list(product(range(N+1), range(N+1)))
    coordinates.remove((0, 0))
    
    # and check all combinations to see if they form a right triangle
    total = 0
    C1 = (0, 0)
    for i in range(len(coordinates)):
        C2 = coordinates[i]
        for j in range(i+1, len(coordinates)):
            C3 = coordinates[j]
            if isRightTriangle(C1, C2, C3):    
                print(C2, C3)
                total += 1
    return total


def gcd(a, b):
    if b > a:
        return gcd(b, a)
    if a % b == 0:
        return b
    return gcd(b, a%b)


# C1 = (0, 0) is fixed
# given a coordinate C2 = (x, y) we are going to calculate the number of C3 that form a right triangle
# to do this, imagine exending the perpendicular line from the top of C2
# the number of right triangles is the number of integer grid points this perpendicular line hits
# 
# Notice that this line will always have a negative slope by construction
# therefore, consider what happens to the line as it extends to the bottom right
# either it hits the x-axis or it hits the edge of the grid
# to calculate how many integer grid points it hits, we just take the minimum of these possibilities
def counting(N):
    coordinates = list(product(range(N+1), range(N+1)))
    coordinates.remove((0, 0))

    total = 0
    for x in range(N+1):
        for y in range(N+1):
            if x == 0 and y == 0:
                continue
            # This is a special case because we get a divide by 0 error
            # here we just get a right triangle with the right angle at the axis
            if x == 0 or y == 0:
                total += N
                continue
        
            d = gcd(x, y)
            a, b = y//d, x//d

            total += min( (N-x)//a, y//b )      # number of integer grid poitns of the perpendicular line extending to the bottom right
            total += min( x//a, (N-y)//b )      # number of integer grid poitns of the perpendicular line extending to the top left

    # Now we just have to account for when the right angle of the right triangle occurs at the origin
    # There will be N^2 of these since all C2 = (x, 0) and C3 = (0, y) will form a right triangle
    # and there are N options for both x and y
    total += N**2
    return total


def main(N=50):
    #total = brute_force(N)
    total = counting(N)
    print(f"The number of right triangles that can be formed in an {N} by {N} grid is:", total)
    return total

if __name__ == "__main__":
    main()