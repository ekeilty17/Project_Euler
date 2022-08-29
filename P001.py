
def main(N=1000):
    total = 0
    for x in range(1, N):
        if x % 3 == 0 or x % 5 == 0:
            total += x
    
    print(f"Sum of all multiples of 3 or 5 below {N}:", total)
    return total

if __name__ == "__main__":
    main()