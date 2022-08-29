# integer factorization by Trial Division
def Prime_Factors(n):
    # Error Check
    if type(n) != int and type(n) != long:
        raise TypeError('must be integer')
    if n < 2:
        return []
    factors = []
    # as always, take care of the 2s first bc they are easy
    while n % 2 == 0:
        factors += [2]
        n =  n // 2
    # if n was purely a power of 2, then the function ends here
    if n == 1:
        return factors
    # since we got rid of the 2's potential factors, f can start at 3
    # other than that, this loop is pretty self explainitory
    f = 3
    while f*f <= n:
        if n % f == 0:
            factors += [f]
            n = n // f
        else:
            f += 2
    return factors + [n]


# brute force is pretty fast in this case, are we aren't even using the best prime factorization function
def brute_force(N):

    consecutive = []
    n = 2
    while len(consecutive) < N:
        factors = Prime_Factors(n)
        if len(set(factors)) == N:
            consecutive.append(n)
        else:
            consecutive = []
        n += 1
    
    return consecutive

def main(N=4):

    consecutive = brute_force(N)
    print(f"The first four consecutive integers to have four distinct prime factors are:", consecutive)
    return consecutive

if __name__ == "__main__":
    main()