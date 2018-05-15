def concat(L):
    out = ""
    for t in L:
        for n in t:
            out += str(n)
    return int(out)

def numDigits(n):
    accum = 0
    while n != 0:
        n /= 10
        accum += 1
    return accum

def MagicTriangle(t):
    #Below is NOT the numbers, they are the indeces of the nodes
    #
    #   0
    #    \
    #     1
    #    / \
    #   4 _ 2 _ 3
    #  /
    # 5
    #
    #define leaf as a node that branches out from the base
    #to convert this to a unique list, start with the lowest index leaf 
    #   and make a truple going into the base
    #This becomes: (0, 1, 2), (3, 2, 4), (5, 2, 1)
    
    #given that they all need to sum up to t
    #0 is completely free
    #1 is free but can't be 0
    #2 is forced
    #3 is free but can't be 0, 1, or 2
    #4 and 5 are forced
    #a final retriction is that T0 < T3 and T0 < T5
    out = []
    for T0 in range(1,7):
        for T1 in range(1,7):
            T2 = t - T1 - T0
            for T3 in range(1,7):
                T4 = t - T2 - T3
                T5 = t - T1 - T4
                #This ensures my solutions are unique
                if T0 > T5 or T0 > T3:
                    continue
                if list(sorted([T0, T1, T2, T3, T4, T5])) == [1,2,3,4,5,6]:
                    if T0 + T1 + T2 == T3 + T2 + T4 == T1 + T4 + T5 == t:
                        out += [[(T0, T1, T2), (T3, T2, T4), (T5, T4, T1)]]
    return out

"""
Solutions = []
for i in range(9,13):
    Solutions += MagicTriangle(i)

Solutions = [concat(s) for s in Solutions]
for s in Solutions:
    print s
print
print max(Solutions)
"""

def MagicPentagon(t):
    #       0
    #        \
    #         1   3
    #       /   \ |
    #     8       2
    #   / |       |
    # 9   6 _____ 4 __ 5
    #     |
    #     7
    #
    # This becomes (0, 1, 2), (3, 2, 4), (5, 4, 6), (7, 6, 8), (9, 8, 1)
    #
    # 0 is completely free
    # 1 is free but cannot be 0
    # 2 is forced but cannot be previous
    # 3 is free but cannot be previous
    # 4 is forced ""   ""
    # 5 is free ""   ""
    # 6 is forced ""   ""
    # 7 is free ""   ""
    # 8 is forced ""  ""
    # 9 is forced ""  ""
    out = []
    for T0 in range(1,11):
        for T1 in range(1,11):
            T2 = t - T0 - T1
            for T3 in range(1,11):
                if T0 > T3:
                    continue
                T4 = t - T2 - T3
                for T5 in range(1,11):
                    if T0 > T5:
                        continue
                    T6 = t - T4 - T5
                    for T7 in range(1,11):
                        T8 = t - T6 - T7
                        T9 = t - T1 - T8
                        if T0 > T7 or T0 > T9:
                            continue
                        if list(sorted([T0, T1, T2, T3, T4, T5, T6, T7, T8, T9])) == [1,2,3,4,5,6,7,8,9,10]:
                            if T0 + T1 + T2 == T3 + T2 + T4 == T5 + T4 + T6 == T7 + T6 + T8 == T9 + T8 + T1 == t:
                                out += [[(T0, T1, T2), (T3, T2, T4), (T5, T4, T6), (T7, T6, T8), (T9, T8, T1)]]
    return out

Solutions = []
#min possible is 1+2+3=6 and max possible is 8+9+10 = 27
for i in range(6,28):
    Solutions += MagicPentagon(i)

for s in Solutions:
    print s
print

Solutions = [concat(s) for s in Solutions]
for s in Solutions:
    print s
print

Solutions_16 = [s for s in Solutions if numDigits(s) == 16]
for s in Solutions_16:
    print s
print

print max(Solutions_16)
