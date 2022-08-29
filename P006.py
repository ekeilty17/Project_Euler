def brute_force(N):

    sum_squares = 0
    sum_ = 0
    for i in range(1, N+1):
        sum_ += i
        sum_squares += i**2

    return sum_**2 - sum_squares

# The above is pretty instanteous for the given problem, but we can do even better
def constant_time(N):
    sum_of_squares = N*(N+1)*(2*N+1)//6
    square_of_sum = N**2*(N+1)**2//4       # square of sum = sum of cubes
    return square_of_sum - sum_of_squares

def main(N=100):

    #s = brute_force(N)
    s = constant_time(N)

    print(f"The difference between the sum of square and square of sums for the first {N} natural numbers:", s)
    return s

if __name__ == "__main__":
    main(100)