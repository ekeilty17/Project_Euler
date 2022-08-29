def isPalindrome(n):
    s = str(n)
    for i in range(len(s)):
        if s[i] != s[-(i+1)]:
            return False
    return True

def naive_search(N):
    """
    This is just a brute force search looking at all possible (a, b) pairs
    """
    a = b = 10**(N-1)
    
    max_palindrome = 1
    while a < 10**N:
        if isPalindrome(a*b):
            if a*b > max_palindrome:
                print(a, b, a*b)
                max_palindrome = a*b
        if b >= 10**N:
            a += 1
            b = a
        else:
            b += 1
    
    return max_palindrome


def efficient_search(N):
    """
    We search over the diagonal (a, a-offset)

      1     2     3     4     5     6     7     8     9     10    11    12    13    14    15    16    17    18    19    
            4     6     8     10    12    14    16    18    20    22    24    26    28    30    32    34    36    38    
                  9     12    15    18    21    24    27    30    33    36    39    42    45    48    51    54  / 57    
                        16    20    24    28    32    36    40    44    48    52    56    60    64    68  / 72    76    
                              25    30    35    40    45    50    55    60    65    70    75    80  / 85    90    95    
                                    36    42    48    54    60    66    72    78    84    90  / 96    102   108   114   
                                          49    56    63    70    77    84    91    98  / 105   112   119   126   133   
                                                64    72    80    88    96    104 / 112   120   128   136   144   152   
                                                      81    90    99    108 / 117   126   135   144   153   162   171   
                                                            100   110 / 120   130   140   150   160   170   180   190   
                                                              --> 121   132   143   154   165   176   187   198   209   
                                                                      \ 144   156   168   180   192   204   216   228   
                                                                           \  169   182   195   208   221   234   247   
                                                                                  \ 196   210   224   238   252   266   
                                                                                       \  225   240   255   270   285   
                                                                                              \ 256   272   288   304   
                                                                                                   \  289   306   323   
                                                                                                          \ 324   342   
                                                                                                               \  361 
    
    Once a palindrome a*b is found, we can prune off all other numbers not inside the triangle denoted by / and \ 
    Then, we increment the offset and search the next diagonal, stopping either once we hit a palindrone or go above the diagonal
    
    This is because a > b implies (a+1)(b-1) < ab, so we can rule out the top diagonal of the triangle,
    and we already checked the bottom diagonal because we stop at the first palindrome we find on the diagonal
    """
    
    U = 10**N               # upperbound on palindromes
    diagonal = [(1, 1)]     # diagonal of triangle
    offset_upperbound = U   # will allow us to stop once we hit the top right corner of the triangle

    max_palindrome = 1
    for offset in range(0, U):
        # if we've broken out of the triangle with the offset, we can stop
        if offset > offset_upperbound:
            break

        # iterating over diagonals starting with largest values
        for a in reversed(range(1, U)):
            b = a - offset
            # since values of monotonic on the diagonal, once we are smaller than max_palindrome, we will always be smaller, so we stop
            if a*b <= max_palindrome:
                break
            # if we break out of the triangle, stop
            if (a, b) in diagonal:
                break
            # since values of monotonic on the diagonal, once we find a palindrome, it will be the largest on the diagonal, so we stop
            if isPalindrome(a*b):
                print(a, b, a*b)
                max_palindrome = a*b

                # adjust bounds of triangle
                diagonal = [(a+c, b-c) for c in range(U - a)]
                offset_upperbound = 2*U - a - b
                break
    
    return max_palindrome

    
def main(N=3):

    #max_palindrome = naive_search(N)
    max_palindrome = efficient_search(N)
    
    print(f"The largest palindrome made from the product of two {N}-digit numbers:", max_palindrome)
    return max_palindrome    

if __name__ == "__main__":
    main()