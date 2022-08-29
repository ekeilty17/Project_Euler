import math

# How does this work
#   We can decompose sqrt(n) as:        sqrt(n) = 10*A + B
#   Therefore                           n = (10*A + B)^2 = 100*A^2 + 20AB + B^2
#   
#   We can update our approximation of sqrt(n) by finding the largest B we can add
def sqrt_by_hand(n, d):
    
    # putting n in a more usable form
    digits = [int(d) for d in str(n) if d != '.']
    if len(digits) % 2 == 1:
        digits = [0] + digits
    
    sqrt = 0
    remainder = 0

    while len(str(sqrt)) < d:

        # bring down next two digits
        remainder = 100*remainder + 10*digits[0] + digits[1]

        # adding zeros to end of number for next iterations
        digits = digits[2:] + [0, 0]

        # finding largest B s.t. 20*A*B + B^2 <= remainder
        B = 0
        while 20*sqrt*B + B**2 <= remainder:
            B += 1
        B -= 1

        # y is what goes under the number that was brought down
        y = 20*sqrt*B + B**2

        # update the remainder
        remainder -= y

        # x is the next digit in the sqrt
        sqrt = 10*sqrt + B
    

    # This is just putting the results in a nice form
    non_decimal_part = str(int(math.sqrt(n)))
    sqrt_str = str(sqrt)
    sqrt_str = sqrt_str[:len(non_decimal_part)] + '.' + sqrt_str[len(non_decimal_part):]

    # return in the form of a string
    return sqrt_str

def digital_sum(x):
    return sum([int(d) for d in str(x) if d != "."])

def main(N=100, d=100):

    total = 0
    squares = [n**2 for n in range(1, int(math.sqrt(N))+2)]
    for n in range(1, N+1):
        if n in squares:
            continue

        sqrt_n = sqrt_by_hand(n, d)
        total += digital_sum(sqrt_n)

    print(f"The digital sum of the first {d} digits of all irrational square roots under {N} is:", total)
    return total

if __name__ == "__main__":
    main()