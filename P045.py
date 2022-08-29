import math

def Triangle(n):
    return (n*(n+1)) // 2

# See P042.py for the math behind this
def isTriangle(x):
    n = (-1 + math.sqrt(8*x+1))/2
    return x == Triangle(math.floor(n)) or x == Triangle(math.ceil(n))


def Pentagon(n):
    return (n*(3*n-1)) // 2

# See P044.py for the math behind this
def isPentagon(x):
    n = (1 + math.sqrt(24*x + 1)) / 6
    return x == Pentagon(math.floor(n)) or x == Pentagon(math.ceil(n))


def Hexagon(n):
    return n*(2*n-1)

# n * (2*n - 1) = x
# 2n^2 - n = x
# n^2 - 1/2 * n = x/2
# (n - 1/4)^2 = x/2 + 1/16
# n = 1/4 + sqrt(x/2 + 1/16)
# N = (1 + sqrt(8x + 1)) / 4

def isHexagon(x):
    n = (1 + math.sqrt(8*x + 1)) / 4
    return x == Hexagon(math.floor(n)) or x == Hexagon(math.ceil(n))

def main(N=3):

    TPH_numbers = []
    Tn = 0
    
    while len(TPH_numbers) < N:
        Tn += 1
        x = Triangle(Tn)
        if isPentagon(x) and isHexagon(x):
            TPH_numbers.append( x )
    
    print(f"The next triangle number that is also pentagonal and hexagonal is:", TPH_numbers[-1])
    return TPH_numbers[-1]

if __name__ == "__main__":
    main()