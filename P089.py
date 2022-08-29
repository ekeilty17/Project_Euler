# Basic Rules of Roman Numerals
#   1) Numerals must be written in descending order
#   2) M, C, and X must not be equalled or exceeded by smaller demoninations
#   3) D, L, and V can only appear once

# But then we want subtractive combinations, so we add these rules
#   4) Only one I, X, C can be used as the leading numeral in a subtractive pair
#   5) I can only be placed before V and X
#   6) X can only be placed before L and C
#   7) C can only be placed before D and M

roman_to_arabic = { 'I' : 1,
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
def isroman_to_arabicidRomanNumeral(R):
    # Numerals must be written in descending order
    if R != "".join( sorted(R, key = lambda x: -roman_to_arabic[x]) ):
        return False
    
    # M, C, and X must not be equalled or exceeded by smaller demoninations
    if roman_to_arabic['I'] * R.count('I') >= roman_to_arabic['X'] or roman_to_arabic['V'] * R.count('V') >= roman_to_arabic['X']:
        return False
    if roman_to_arabic['X'] * R.count('X') >= roman_to_arabic['C'] or roman_to_arabic['L'] * R.count('L') >= roman_to_arabic['C']:
        return False
    if roman_to_arabic['C'] * R.count('C') >= roman_to_arabic['M'] or roman_to_arabic['D'] * R.count('D') >= roman_to_arabic['M']:
        return False
    
    # D, L, and V can only appear onces
    if R.count('V') > 1 or R.count('L') > 1 or R.count('D') > 1:
        return False

    return True
print isroman_to_arabicidRomanNumeral('MMMMDCLXVII')
"""

def RomanToArabic(R):
    
    #if not isroman_to_arabicidRomanNumeral(R):
    #   return False
    
    total = 0
    i = 0
    while i < len(R):
        
        if i < len(R) - 1 and R[i:i+2] in ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']:
            total += roman_to_arabic[R[i:i+2]]
            i += 2
        else:
            total += roman_to_arabic[R[i]]
            i += 1

    return total

def minRomanNumeral(n):
    
    R = ""
    while n > 0:
        # recall
        #   - C can only be placed before D and M
        #   - X can only be placed before L and C
        #   - I can only be placed before V and X
        # Therefore, we just add the largest possible roman digit we can add (i.e. greedy algorithm)
        for roman_digit, value in reversed(sorted(roman_to_arabic.items(), key=lambda t: t[1])):
            if n >= value:
                R += roman_digit
                n -= value
                break
    
    return R

# counting the total number of characters in a list of strings
def total_characters(L):
    return sum([len(x) for x in L])

def main(roman_numerals):

    roman_numerals_minimal = []
    for R in roman_numerals:
        n = RomanToArabic(R)
        R_minimal = minRomanNumeral(n)
        roman_numerals_minimal.append( R_minimal )
        #print(n, R, R_minimal)
    
    diff = total_characters(roman_numerals) - total_characters(roman_numerals_minimal)
    print(f"The number of characters saved by writing each of the roman numerals in their minimal form is:", diff)

if __name__ == "__main__":
    # reading files
    with open("p089_roman.txt",'r') as f:
        lines = f.readlines()
    
    # cleaning inputs
    roman_numerals = [line.strip() for line in lines]

    # getting solution
    main(roman_numerals)