import numpy as np

# We can do basically the same thing as P077.py
# the problem with this is N is way too large, so it's very very slow
def naive_search(N):
    partitions = np.zeros((N+1, N+1), dtype=int)
    partitions[0, :] = 1                # base-case: number of ways to make a total of 0 is 1...do nothing
    
    n = 0
    while partitions[n, -1] % N != 0:
        #print(n)
        n += 1
        for i in range(N+1):
            partitions[n, i] = partitions[n, i-1]
            if n >= i:
                partitions[n, i] += partitions[n-i, i]
    
    print(n)
    return n, partitions[n, -1]

# Using the recurrance relation:
#   p(n) = p(n-1) + p(n-2) - p(n-5) - p(n-7) + p(n-12) + p(n-15) - ...
#        = SUM{ (-1)^{k+1} p( n - Pentagon(k) ) } for k != 0
#
# Source: https://en.wikipedia.org/wiki/Partition_function_(number_theory)

def Pentagon(n):
    return (n*(3*n-1)) // 2

def P(N):
    partitions = [0] * (N+1)
    partitions[0] = 1

    for i in range(1, N+1):
        for j in range(i, N+1):
            partitions[j] += partitions[j - i]

    #print(partitions)
    return partitions[N]

def P_mod_m_with_memoization(n, m, p):
    if n < 0:
        return 0, p
    if n < len(p):
        return p[n], p
    if n == 0:
        p = [1]
        return 1, p
    if n == 1:
        p = [1, 1]
        return 1, p
    
    total = 0
    k = 1
    while Pentagon(k) <= n:
        p_n, p = P_mod_m_with_memoization(n - Pentagon(k), m, p)
        total += int( (-1)**(k+1) * p_n )
        k += 1
    
    k = -1
    while Pentagon(k) <= n:
        p_n, p = P_mod_m_with_memoization(n - Pentagon(k), m, p)
        total += int( (-1)**(k+1) * p_n )
        k -= 1
    
    total %= m
    p.append(total)
    return total, p

def efficient_search(N):

    n = 1
    p = [1, 1]
    while p[n] % N != 0:
        n += 1
        _, p = P_mod_m_with_memoization(n, N, p)
        #print(n, p[n])
    
    return n

def main(N=10**6):

    #n = naive_search(N)
    n = efficient_search(N)
    print(f"The first number for which its partitions are divisible by {N} is:", n)
    return n

if __name__ == "__main__":
    main()