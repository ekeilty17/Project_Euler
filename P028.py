# to add to a list in a spiral fashion
def add_right(L, a):
    for i in range(len(a)):
        L[i] += [a[i]]
    return L

def add_bottom(L, a):
    return L + [list(reversed(a))]

def add_left(L, a):
    a = list(reversed(a))
    for i in range(len(a)):
        L[i] = [a[i]] + L[i]
    return L

def add_top(L, a):
    return [a] + L

# generates nxn spiral (n can only be odd)
def gen_spiral(n):
    if n <= 0:
        return []
    if n % 2 == 0:
        return []
    if n == 1:
        return [[1]]

    out = gen_spiral(n-2)
    nxt = out[0][len(out[0])-1] + 1
    
    out = add_right(out, list(range(nxt, nxt+n-2)))
    nxt += n-2

    out = add_bottom(out, list(range(nxt, nxt+n-1)))
    nxt += n-1

    out = add_left(out, list(range(nxt, nxt+n-1)))
    nxt += n-1
    
    out = add_top(out, list(range(nxt, nxt+n)))

    return out


def main(N=1000):
    
    spiral = gen_spiral(N+1)

    # summing diagonals
    total = 0
    total += sum([spiral[i][i] for i in range(len(spiral))])                            # top left to bottom right
    total += sum([spiral[-i-1][i] for i in range(len(spiral)) if i != len(spiral)//2])  # bottom left to top right

    print(f"The sum of the diagonals in a {N+1}x{N+1} prime spiral is:", total)
    return total

if __name__ == "__main__":
    main()