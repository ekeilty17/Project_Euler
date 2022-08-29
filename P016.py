
# Python can just solve this one, and I'm not really sure how else I'm supposed to do it
def cheating(N):
    return sum([int(d) for d in str(2**N)])

def main(N=1000):
    s = cheating(N)
    print(f"Sum of the digits in 2^{N}:", s)
    
if __name__ == "__main__":
    main()
