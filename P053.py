def factorial_list(n):
    out = [1]
    f = 1
    for i in range(1, n+1):
        f *= i
        out += [f]
    return out

# This is actually very fast
def brute_force_simple(N, n):
    F = factorial_list(n)

    total = 0
    for k in range(1, n+1):
        for r in range(1, k+1):
            kCr = (F[k] // F[k-r]) // F[r]
            if kCr > N:
                total += 1
    
    return total


# But there are some tricks we can do to save even more time
def brute_force_efficient(N, n):
    F = factorial_list(n)

    total = 0
    for k in range(1, n+1):
        m = k//2
        for r in reversed(range(1, m+1)):
            kCr = (F[k] // F[k-r]) // F[r]
            if kCr > N:
                # we can use the fact that kCr = kC{k-r}
                total += 1 if (r == m and k % 2 == 1) else 2
            else:
                # and that kCr monotonically increases up until the mid point
                # so by iterating backwards, once we are <= N, we can just break
                break
    
    return total



def main(N=10**6, n=100):
    total = brute_force_efficient(N, n)
    
    print(f"The number of values (not necessarily distinct) of nCr for 1 <= n <= {n} that are greater than {N} is:", total)
    return total

if __name__ == "__main__":
    main()