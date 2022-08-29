# It turns out python can just do this
def cheating(a, e, d):
    return (a * 2**e + 1) % (10**d)

# This is really the hard part of the problems
def modular_exponentiation(b, e, m):
    b = b % m
    if b == 0:
        return 0
    
    ans = 1         # = b^e mod m
    while e > 0:
        # If e is odd, multiply n with result
        if e % 2 == 1:
            ans = (ans * b) % m
 
        # e must be even now
        e = e // 2
        b = (b * b) % m
    
    return ans

def main(a=28433, e=7830457, d=10):
    #result = cheating(a, e, d)
    result = modular_exponentiation(2, e, 10**d)
    result = (a * result + 1) % 10**d
    
    print(f"The last {d} digits of {a} * 2^{e} + 1 is:", result)
    return result

if __name__ == "__main__":
    main()