def factorial(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    return n*factorial(n-1)

# Python can just do this, but I'm not sure how else I would do it because this is pretty fast
def cheating(n):
    f = factorial(n)
    return sum(int(d) for d in str(f))

def main(N=100):
    total = cheating(N)
    print(f"The sum of the digits {N}! is:", total)
    return total

if __name__ == "__main__":
    main()
