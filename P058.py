def isPrime(n):
    if n <= 0:
        return False
    if n == 1:
        return False
    first_few = [      2,   3,   5,   7,  11,  13,  17,  19,  23,  29,  31,  37,  41,  43,  47,
                      53,  59,  61,  67,  71,  73,  79,  83,  89,  97, 101, 103, 107, 109, 113,
                     127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]
    if n in first_few:
        return True
    for i in range(2, int(n**(0.5))+1):
        if n % i == 0:
            return False
    return True

# We calculate the next number along the diagonals
def diagonals(n):
    if n == 1:
        return [1]
    return [n*n-3*(n-1), n*n-2*(n-1), n*n-1*(n-1), n*n-0*(n-1)]

# this is kinda slow, but good enough for me
def search(N):
    num_primes = 3
    total = 5
    side_length = 3
    while num_primes/total > N/100:
        side_length += 2
        total += 4
        for d in diagonals(side_length)[:-1]:       # don't include the last diagonal because it's n^2
            if isPrime(d):
                num_primes += 1

    return side_length

def main(N=10):

    side_length = search(N)
    print(f"The side length of the square spiral for which the ratio of primes along both diagonals first falls below {N}% is:", side_length)
    return side_length

if __name__ == "__main__":
    main()