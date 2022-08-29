import itertools

def numberify(digits):
    return int( "".join([str(d) for d in digits]) )

def hasProperty(digits):
    return  numberify(digits[1:4]) % 2 == 0  and numberify(digits[2:5]) % 3 == 0 and \
            numberify(digits[3:6]) % 5 == 0  and numberify(digits[4:7]) % 7 == 0 and \
            numberify(digits[5:8]) % 11 == 0 and numberify(digits[6:9]) % 13 == 0 and \
            numberify(digits[7:10]) % 17 == 0

# The brute force is pretty fast
# There's probably some better way to do it, but it's good enough for me
def brute_force():
    pandigital_numbers = []
    for perm in itertools.permutations(list(range(10))):
        if hasProperty(perm):
            pandigital_numbers.append( numberify(perm) )
    return pandigital_numbers

def main():
    
    pandigital_numbers = brute_force()

    print(f"The sum of all 0 to 9 pandigital numbers with this property is:", sum(pandigital_numbers))
    return sum(pandigital_numbers)

if __name__ == "__main__":
    main()