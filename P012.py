def Triangle(n):
    total = 0
    for i in range(1, n+1):
        total += i
    return total

def factors(n):
    if n == 0:
        return []
    if n < 0:
        n *= -1
    if n == 1:
        return [1]
    f = [1, n]
    for i in range(2, n//2+1):
        if n % i == 0:
            f += [i]
    return sorted(f)

def num_factors(n):
    f = 1
    counter = 0
    while n % 2 == 0:
        counter += 1
        n = n//2
    f *= (counter + 1)
    p = 3
    while n != 1:
        counter = 0
        while n % p == 0:
            counter += 1
            n = n//p
        f *= (counter + 1)
        p += 2
    return f

def brute_force(N):
    f = []
    f_num = len(f)
    T = 0
    i = 0
    while f_num < N:
        i += 1
        T += i
        #f = factors(T)
        #f_num = len(f)
        f_num = num_factors(T)      # finding the number of factors is faster than finding the actaual factors
    
    return T

def main(N=500):
    T = brute_force(N)
    print(f"The smallest triangle number with over {N} divisors:", T)
    return T

if __name__ == "__main__":
    main(500)