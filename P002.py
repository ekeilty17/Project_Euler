
# takes too long for large problems
def fibo_rec(n):
    if n < 0:
        return 0
    if n == 1:
        return 1
    return fibo(n-1) + fibo(n-2)


def main(N=4*10**6):

    f1, f2 = 1, 1
    total = 0

    while f2 < N:
        #checking if it's even
        if f2 % 2 == 0:
            total += f2
        
        # next fibonacci pair
        f1, f2 = f2, f1+f2
    
    print(f"Sum of even-valued fibonacci numbers below {N}", total)
    return total

if __name__ == "__main__":
    main()