def Collatz(n):
    count = 1
    out = ""
    while n != 1:
        out += str(n) + " -> "
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3*n + 1
        count += 1
    out += "1"
    #print(out)
    return count

def Collatz_memoized(n, Chains):
    if n == 1:
        Chains[1] = 1
    if n in Chains:
        return Chains[n]
    elif n % 2 == 0:
        Chains[n] = Collatz_memoized(n // 2, Chains) + 1
    else:
        Chains[n] = Collatz_memoized(3*n + 1, Chains) + 1
    return Chains[n]

def brute_force(N):
    max_chain = 0
    max_chain_num = 1
    for i in range(1, N+1):
        C = Collatz(i)
        print(i, C)
        if C > max_chain:
            max_chain = C
            max_chain_num = i

    return max_chain_num

def efficient(N):
    Chains = {}
    for n in range(1, N+1):
        Collatz_memoized(n, Chains)     # Chain is updated
    
    start_num, chain_length = max(Chains.items(), key=lambda t: t[1])
    return start_num

def main(N=10**6):

    #start_num = brute_force(N)
    start_num = efficient(N)
    print(f"The starting number under {N} producing the longest chain:", start_num)
    

if __name__ == "__main__":
    main()