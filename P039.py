import math
from collections import defaultdict

def get_pythagorean_triples_under_perimeter(P):
    # P is the maximum perimeter length
    perfect_squares = set([x**2 for x in range(1, P)])

    triples = set()
    for a in range(1, P//2+1):
        for b in range(a, P//2+1):
            c_2 = a**2 + b**2                   # pythagorean theorem
            if c_2 in perfect_squares:          # if c**2 is a perfect square
                c = int(math.sqrt(c_2))
                if a+b+c <= 1000:
                    triples.add( (a, b, c) )

    return triples

def main(N=1000):

    triples = get_pythagorean_triples_under_perimeter(N)
    #triples = list(sorted(triples, key=lambda t: sum(t)))
    
    D = defaultdict(list)
    for a, b, c in triples:
        D[a+b+c].append( (a, b, c) )
    
    p_max, p_max_triples = max(D.items(), key=lambda t: len(t[1]))
    print(f"The perimeter of a right angle triangle, p <= {N}, with the maximum number of integer triples is:", p_max)
    return p_max
    
if __name__ == "__main__":
    main()