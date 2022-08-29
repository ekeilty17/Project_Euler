import math

def champernownes_constant_up_to_number(n):
    const = [0]
    for digit in range(1, n+1):
        for d in str(digit):
            const.append(int(d))
    return const

def champernownes_constant_up_to_index(i_max):
    const = [0]
    digit = 0
    i = 0
    while i < i_max:
        digit += 1
        i += len(str(digit))
        for d in str(digit):
            const.append(int(d))
    return const

def generative_method(I):
    # I = list of indices

    """
    In this method, we generate all of champernowne's constant up to a certain point and then just index to get the digits we want
    """

    const = champernownes_constant_up_to_index(max(I))
    digits = [const[i] for i in I]
    return digits

def get_nth_digit(n, d):        # starting at index 0
    return int(str(n)[d])


def incremental_method(I):
    # I = list of indices

    """
    In this method, we incremennt through champernowne's constant until we get to the digits we want
    """

    digits = []
    dec_place = 0
    digit = 0
    for i in sorted(I):
        while dec_place < i:
            digit += 1
            dec_place += len(str(digit))

        # "dec_place" is the index of the right-most digit in "digit"
        # so we need to get the index of i within the digits of "digit"
        d = len(str(digit)) - 1 - (dec_place - i)
        digits.append( get_nth_digit(digit, d) )
    
    return digits

def main(N=7):
    I = [10**e for e in range(N)]

    #digits = generative_method(I)
    digits = incremental_method(I)      # the only difference is this is more space efficient
    
    print(digits)
    prod = math.prod(digits)
    print(f"The product of the Champernowne's Constant digits 1, 10, 100, ..., 10^{N-1} is:", prod)
    return prod
    
if __name__ == "__main__":
    main()