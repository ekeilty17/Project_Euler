ones_and_teens = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
ones_and_teens += ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
hundreds  = [""] + [ones_and_teens[n] + " hundred" for n in range(1, 10)]

digital_group_names = ["", "thousand", "million", "billion", "trillion"]


def number_under_100_to_words(n):
    if n < 0 or n > 99:
        raise ValueError("n must be in range [1, 99] inclusive")
    
    if n == 0:
        return "zero"
    
    word = ""
    if n < 20:      # under 20 is irregular patterns
        word += ones_and_teens[n]
    else:           # pattern: tens-ones
        word += tens[n // 10]
        if n % 10 != 0:
            word += "-" + ones_and_teens[n % 10]
    
    return word


def triple_to_words(n, last=False):
    if n > 999:
        raise ValueError("number must be less than 1000")
    
    # hundreds place
    word = hundreds[n // 100]
    
    # if n is a perfect multiple of 100, we are done
    if n % 100 == 0:
        return word
    
    # last means the last triple in the word
    # if we have other stuff after the 100's place, then we need an "and"
    if last or n // 100 != 0:
        word += " and "
    
    # now we just deal with everything under 100
    word += number_under_100_to_words(n % 100)
    return word


def parse_into_digit_groups(n):
    if n < 1000:
        return [n]
    
    digital_groups = []
    s = str(n)
    for i in range(len(s)-3, 0, -3):
        digital_groups.append( int(s[i:i+3]) )
    
    if 3*len(digital_groups) != len(s):
        diff = len(s) - 3*len(digital_groups)
        digital_groups.append( int(s[:diff]) )
    
    return list(reversed(digital_groups))

def number_to_words(n):
    word = ""
    if n < 0:
        word += "negative "
        n *= -1

    limit = 10**(len(digital_group_names)*3)
    if n >= limit:
        raise NotImplementedError(f"Haven't implemented larger than {limit}")

    # less than 100 has edge cases with "and"
    if n < 100:
        return number_under_100_to_words(n % 100)

    digital_groups = parse_into_digit_groups(n)
    group_index = len(digital_groups)-1

    word = ""
    for triple in digital_groups[:-1]:
        if triple != 0:
            word += triple_to_words(triple) + " " + digital_group_names[group_index] + " "
        group_index -= 1
    
    # the last triple has edge cases with "and"
    if digital_groups[-1] != 0:
        word += triple_to_words(digital_groups[-1], last=True)

    return word

def main(N=1000):
    total = 0
    for n in range(1, N+1):
        word = number_to_words(n)
        #print(n, word)
        letters_only = word.replace(" ", "").replace("-", "")
        total += len(letters_only)
    
    print(f"Number of letters used in writing 1 to {N} in English:", total)
    return total


if __name__ == "__main__":
    main()