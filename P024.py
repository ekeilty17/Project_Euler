from itertools import permutations

# This is fast because how python implemented it, but it's cheating
def cheating(N, i):
    all_lex = list(sorted(permutations(range(N))))
    perm = all_lex[k-1]
    return "".join([str(x) for x in perm])


def factorial(n):
    if n <= 0:
        return 1
    if n == 1:
        return 1
    return n*factorial(n-1)

# Here's the idea

# Observe
#   permutations 0123456789 to 0987654321 are index 0*9! to 1*9!-1 = [0,      362879 ]
#   permutations 1234567890 to 1987654320 are index 1*9! to 2*9!-1 = [362880, 725759 ]
#   permutations 2345678901 to 2987654310 are index 2*9! to 3*9!-1 = [725760, 1088639]
# Therefore, the 1 millionth permutation begins with a 2

# So we can keep narrowing down this range through this exact same logic

def logical(N, k):

    nums = list(range(N))
    perm = []
    for i in reversed(range(N)):
        f = factorial(i)
        c = (k-1) // f
        perm += [nums[c]]
        del nums[c]
        k -= c*f

    return "".join([str(x) for x in perm])

def main(N=10, k=10**6):
    if k > factorial(N):
        raise ValueError(f"index cannot be larger than {N}!")
    
    #perm = cheating(N, k)
    perm = logical(N, k)

    print(f"The {N} lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8, and 9 is:", perm)
    return perm

if __name__ == "__main__":
    main()