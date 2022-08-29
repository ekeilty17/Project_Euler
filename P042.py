import math

character_value = {
            '"': 0,
            ',': 0,
            'A': 1,
            'B': 2,
            'C': 3,
            'D': 4,
            'E': 5,
            'F': 6,
            'G': 7,
            'H': 8,
            'I': 9,
            'J': 10,
            'K': 11,
            'L': 12,
            'M': 13,
            'N': 14,
            'O': 15,
            'P': 16,
            'Q': 17,
            'R': 18,
            'S': 19,
            'T': 20,
            'U': 21,
            'V': 22,
            'W': 23,
            'X': 24,
            'Y': 25,
            'Z': 26
            }

def word_value(word):
    return sum([character_value[c] for c in word])

def Triangle(n):
    return (n*(n+1)) // 2

# We can do some math to get n from x
#   n(n+1)/2 = x
#   n^2 + n = 2x
#   (n + 1/2)^2 = 2x + 1/4
#   n = -1/2 + sqrt(2x+ 1/4)              # we only take the positive since n can't be negative
#   n = 1/2 (-1 + sqrt(8x + 1) )

def isTriangle(x):
    n = (-1 + math.sqrt(8*x+1))/2
    return x == Triangle(math.floor(n)) or x == Triangle(math.ceil(n))

def main(words):
    
    triangle_words = []
    for word in words:
        x = word_value(word)
        if isTriangle(x):
            triangle_words.append( word )
    
    print(f"The number of triangle words in the given text file is:", len(triangle_words))
    return len(triangle_words)

if __name__ == "__main__":
    with open('p042_words.txt', 'r') as f:
        words = f.readlines()
        words = words[0].split(",")
    
    main(words)