# preparing the matrix to make it usable
f=open("p089_roman.txt",'r')

L = []
lines = f.readlines()
for line in lines:
    L += [line.split('\n')[0]]

f.close()


# Basic Rules of Roman Numerals
#   1) Numerals must be written in descending order
#   2) M, C, and X must not be equalled or exceeded by smaller demoninations
#   3) D, L, and V can only appear once

# But then we want subtractive combinations, so we add these rules
#   4) Only one I, X, C can be used as the leading numeral in a subtractive pair
#   5) I can only be placed before V and X
#   6) X can only be placed before L and C
#   7) C can only be placed before D and M

val =   {   'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000,
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900
        }
# It'd be fun to write this function, but it's not needed for this problem
"""
def isValidRomanNumeral(R):
    # Numerals must be written in descending order
    if R != "".join( sorted(R, key = lambda x: -val[x]) ):
        return False
    
    # M, C, and X must not be equalled or exceeded by smaller demoninations
    if val['I'] * R.count('I') >= val['X'] or val['V'] * R.count('V') >= val['X']:
        return False
    if val['X'] * R.count('X') >= val['C'] or val['L'] * R.count('L') >= val['C']:
        return False
    if val['C'] * R.count('C') >= val['M'] or val['D'] * R.count('D') >= val['M']:
        return False
    
    # D, L, and V can only appear onces
    if R.count('V') > 1 or R.count('L') > 1 or R.count('D') > 1:
        return False

    return True
print isValidRomanNumeral('MMMMDCLXVII')
"""

def RomanToArabic(R):
    
    #if not isValidRomanNumeral(R):
    #   return False
    
    accum = 0
    i = 0
    while i < len(R):
        
        if i < len(R) - 1 and R[i:i+2] in ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']:
            accum += val[R[i:i+2]]
            i += 2
        else:
            accum += val[R[i]]
            i += 1

    return accum

def minRomanNumeral(n):
    
    out = ""
    while n > 0:
        # C can only be placed before D and M
        if n >= val['M']:
            out += 'M'
            n -= val['M']
        elif n >= val['CM']:
            out += 'CM'
            n -= val['CM']
        elif n >= val['D']:
            out += 'D'
            n -= val['D']
        elif n >= val['CD']:
            out += 'CD'
            n -= val['CD']
        # X can only be placed before L and C
        elif n >= val['C']:
            out += 'C'
            n -= val['C']
        elif n >= val['XC']:
            out += 'XC'
            n -= val['XC']
        elif n >= val['L']:
            out += 'L'
            n -= val['L']
        elif n >= val['XL']:
            out += 'XL'
            n -= val['XL']
        # I can only be placed before V and X
        elif n >= val['X']:
            out += 'X'
            n -= val['X']
        elif n >= val['IX']:
            out += 'IX'
            n -= val['IX']
        elif n >= val['V']:
            out += 'V'
            n -= val['V']
        elif n >= val['IV']:
            out += 'IV'
            n -= val['IV']
        elif n >= val['I']:
            out += 'I'
            n -= val['I']
    
    return out

# number of characters in R
def numCharacters(L):
    accum = 0
    for x in L:
        accum += len(x)
    return accum

reduced = []
for R in L:
    print R, RomanToArabic(R) 
    reduced += minRomanNumeral(RomanToArabic(R))


print numCharacters(L) - numCharacters(reduced)
