def MagicTriangle(S):
    # Below is NOT the numbers, they are the indeces of the nodes
    #
    #   0
    #    \
    #     1
    #    / \
    #   4 _ 2 _ 3
    #  /
    # 5
    #
    # define leaf as a node that branches solution_sets from the base
    # to convert this to a unique list, start with the lowest index leaf 
    #   and make a truple going into the base
    # This becomes: (0, 1, 2), (3, 2, 4), (5, 2, 1)
    #
    # given that they all need to sum up to S
    #   0 is completely free
    #   1 is free but can't be 0
    #   2 is forced
    #   3 is free but can't be 0, 1, or 2
    #   4 is forced
    #   5 is forced
    #
    # a final retriction is that T0 < T3 and T0 < T5 to make solutions unique
    solution_sets = []
    for T0 in range(1, 7):
        for T1 in range(1, 7):
            T2 = S - T1 - T0
            for T3 in range(1, 7):
                T4 = S - T2 - T3
                T5 = S - T1 - T4
                # This ensures my solutions are unique
                if T0 > T5 or T0 > T3:
                    continue
                if list(sorted([T0, T1, T2, T3, T4, T5])) == list(range(1, 7)):
                    if T0 + T1 + T2 == T3 + T2 + T4 == T1 + T4 + T5 == S:
                        solution_sets.append( [(T0, T1, T2), (T3, T2, T4), (T5, T4, T1)] )
    return solution_sets


def MagicPentagon(S):
    # Below is NOT the numbers, they are the indeces of the nodes
    #
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
    # given that they all need to sum up to S
    #   0 is completely free
    #   1 is free but can't be 0
    #   2 is forced
    #   3 is free but can't be 0, 1, or 2
    #   4 is forced
    #   5 is free but can't be 0, 1, 2, 3, or 4
    #   6 is forced
    #   7 is free but can't be 0, 1, 2, 3, 4, 5, or 6
    #   8 is forced
    #   9 is forced
    #
    # a final retriction is that T0 < T3 and T0 < T5 and T0 < T7 and T0 < T9 to make solutions unique
    solution_sets = []
    for T0 in range(1, 11):
        for T1 in range(1, 11):
            T2 = S - T0 - T1
            for T3 in range(1, 11):
                # This ensures my solutions are unique
                if T0 > T3:
                    continue
                T4 = S - T2 - T3
                for T5 in range(1, 11):
                    # This ensures my solutions are unique
                    if T0 > T5:
                        continue
                    T6 = S - T4 - T5
                    for T7 in range(1, 11):
                        T8 = S - T6 - T7
                        T9 = S - T1 - T8
                        # This ensures my solutions are unique
                        if T0 > T7 or T0 > T9:
                            continue
                        if list(sorted([T0, T1, T2, T3, T4, T5, T6, T7, T8, T9])) == list(range(1, 11)):
                            if T0 + T1 + T2 == T3 + T2 + T4 == T5 + T4 + T6 == T7 + T6 + T8 == T9 + T8 + T1 == S:
                                solution_sets.append( [(T0, T1, T2), (T3, T2, T4), (T5, T4, T6), (T7, T6, T8), (T9, T8, T1)] )
    return solution_sets


# TODO: We can probably generalize this to do any N-gon, but we don't need to for the question

def concat(L):
    return int( "".join([str(n) for row in L for n in row]) )

def numDigits(n):
    return len(str(n))

def main(N=5, d=16):

    MagicFunc = None
    if N == 3:
        MagicFunc = MagicTriangle
    elif N == 5:
        MagicFunc = MagicPentagon
    else:
        raise ValueError(f"I have not implemented a solution for an n-gon of size {n}")

    # getting the bounds for the possible sums
    minimum_total = sum( list(range(2*N))[:3] )
    maximum_total = sum( list(range(2*N))[-3:] )
    
    # getting solutions for each possible total
    Solutions = []
    for S in range(minimum_total, maximum_total+1):
        Solutions.extend( MagicFunc(S) )

    # concatenating solutions into numbers
    Solutions = [concat(sol) for sol in Solutions]

    # getting solutions with only the appropriate number of digits
    Solutions = [s for s in Solutions if numDigits(s) == d]

    print(f"The maximum {d}-digit string for a 'magic' {N}-gon ring is:", max(Solutions))
    return max(Solutions)

if __name__ == "__main__":
    #main(N=3, d=9)
    main()