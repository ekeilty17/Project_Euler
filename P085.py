# Number of rectanges of a given size (kn by km) that fit in a rectangle of size n by m
def num_rectangles_of_dim(m, n, km, kn):
    return (m - (km-1)) * (n - (kn-1))

# The total number of rectangles of any dimension
def num_rectangles(m, n):
    return sum([num_rectangles_of_dim(m, n, km, kn) for km in range(1, m+1) for kn in range(1, n+1) ])

# The tricky part about this problem is knowing how to prune the search
# Observe that the number of rectangles that can be contained in a grid is monotonically increasing
# Therefore, if our current closest is d away from N, and we get to a grid that contains > N + d rectangles
# Then we know we can stop searching
def brute_force(N):
    closest = abs(N - num_rectangles(1, 1))
    closest_grid = (1, 1)
    R = num_rectangles(1, 1)

    m = 1
    while R <= N + closest:
        
        n = m
        while R <= N + closest:
            
            R = num_rectangles(m, n)
            if abs(N - R) < closest:
                closest = abs(N - R)
                closest_grid = (m, n)
            
            n += 1
        
        m += 1
        R = num_rectangles(m, m)
    
    return closest_grid

def main(N=2*10**6):
    m, n = brute_force(N)

    print(f"The {m} by {n} grid conains {num_rectangles(m, n)} rectangles")
    print(f"The area of rectangular grid which contains the closest number of rectangles to {N} is:", m*n)
    return m*n


if __name__ == "__main__":
    main()