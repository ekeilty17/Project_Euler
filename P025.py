def num_digits(n):
    return len(str(n))  

def main(N=1000):

    index = 2
    f1 = f2 = 1
    while num_digits(f2) < N:
        f1, f2 = f2, f1 + f2
        index += 1

    print(f"The index of the first term in the Fibonacci sequence to contain 1000 digits is:", index)
    return index

if __name__ == "__main__":
    main(1000)
