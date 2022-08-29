import math

def brute_force(N):

    matches = []

    for a in range(N//2):
        for b in range(a, N//2):
            c = math.sqrt(a**2+b**2)
            c = int(c) if c == int(c) else c
            if a+b+c == N:
                print("a =", a)
                print("b =", b)
                print("c =", c)
                print("abc =", a*b*c)
                matches.append( (a, b, c) )
    
    return matches

def main(N=1000):

    triples = brute_force(N)
    print(f"Pythagorean triples with sum of {N}:", triples)
    return triples

if __name__ == "__main__":
    main(1000)