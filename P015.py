
# It you look at it mathematically, it turns out the answer is just 2nCn
# nCr = n!/r!(n-r!)

def factorial(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n < 0:
        return 0
    total = 1
    for i in range(1,n+1):
        total *= i
    return total

def lattice_paths(n):
    return factorial(2*n) // (factorial(n)*factorial(2*n-n))

def main(N=20):
    num_routes = lattice_paths(N)
    print(f"The number of routes in an {N}x{N} grid:", num_routes)
    
if __name__ == "__main__":
    main()
