def DigitalSum(n):
    return sum([int(d) for d in str(n)])

# Dispite 99^99 being a massive number python has no problem computing it, which is why I call this cheating
# but it's very fast and I see no reason to improve it
def cheating(N):

    max_sum = 0
    max_pair = (0, 1)
    for a in range(0, N):
        for b in range(0, N):
            s = DigitalSum(a**b)
            if s > max_sum:
                max_sum = s
                max_pair = (a, b)
    
    print(max_pair, max_pair[0]**max_pair[1])
    return max_sum

def main(N=100):
    
    max_sum = cheating(N)
    print(f"The maximal digital sum of a^b where a, b < {N} is:", max_sum)
    return max_sum

if __name__ == "__main__":
    main()