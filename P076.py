# This is basically the same as problem 31 where we just have a different "coin" set
# So see P031.py for an explanation of the dynamic programming solution

def P(N):

    partitions = [0] * (N+1)
    partitions[0] = 1

    for i in range(1, N+1):
        for j in range(i, N+1):
            partitions[j] += partitions[j - i]

    #print(partitions)
    return partitions[N]

def main(N=100):

    p_n = P(N)
    
    # we have to substract 1 from p(n) because the above function will include just the number itself as a partition
    # but we want the number of ways to write the number as the sum of at least TWO integers
    total = p_n - 1
    print(f"The number of ways that {N} be written as a sum of at least two positive integers is:", total)
    return total

if __name__ == "__main__":
    main()