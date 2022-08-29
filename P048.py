# it turns out python will just do this for you
def cheating(N, d):
    return sum([i**i for i in range(1, N+1)]) % (10**d)


# but that's not the spirit of the question, really what they want is for us to implement modular exponentiation
def modular_exponentiation(n, e, m):
    n = n % m
    if n == 0:
        return 0
    
    ans = 1         # = n^e mod m
    while e > 0:
        # If e is odd, multiply n with result
        if e % 2 == 1:
            ans = (ans * n) % m
 
        # e must be even now
        e = e // 2
        n = (n * n) % m
        
    return ans

def efficient(N, d):
    total = 0
    for i in range(1, N+1):
        total += modular_exponentiation(i, i, 10**d)
    return total % (10**d)

def main(N=1000, d=10):
    #total = cheating(N, d)
    total = efficient(N, d)

    print(f"The last {d} digits of the sum 1^1 + 2^2 + ... + {N}^{N} is:", total)
    return total


if __name__ == "__main__":
    main()