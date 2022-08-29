def getDigits(n):
    return [int(d) for d in str(n)]

def main():

    x_max = []
    for x in range(1, 10**5):       # since n > 1, we must be concatenating at least one 4-digit and one 5-digit number
        digits = []
        for n in range(1, 10):
            digits += getDigits(n*x)
            if list(sorted(digits)) == list(range(1, 10)):
                x_max = digits
                break
            elif len(digits) > 10:
                break

    x_max = "".join([str(d) for d in x_max])

    print(f"The largest pandigital 9-digit number that can be formed as the concatenatation of consecutive integer products is:", x_max)
    return x_max
    

if __name__ == "__main__":
    main()