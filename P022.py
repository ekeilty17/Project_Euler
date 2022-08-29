#getting alphabetical value
alpha = {
        "A": 1,
        "B": 2,
        "C": 3,
        "D": 4,
        "E": 5,
        "F": 6,
        "G": 7,
        "H": 8,
        "I": 9,
        "J": 10,
        "K": 11,
        "L": 12,
        "M": 13,
        "N": 14,
        "O": 15,
        "P": 16,
        "Q": 17,
        "R": 18,
        "S": 19,
        "T": 20,
        "U": 21,
        "V": 22,
        "W": 23,
        "X": 24,
        "Y": 25,
        "Z": 26
    }

def alpha_value(name):
    return sum([alpha[char] for char in name])

def main(names):
    total_score = 0
    for name in names:
        # have to increment the index by 1 bc index starts at 0
        total_score += (names.index(name)+1) * alpha_value(name)

    print(f"The total of all the name scores in the file is:", total_score)
    return total_score

if __name__ == "__main__":
    
    # preprocessing names file into nice format
    with open("p022_names.txt",'r') as f:
        names = f.readlines()[0].split(',')
    names = [name[1:-1] for name in names]
    names.sort()

    main(names)