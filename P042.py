alpha = {
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

def word2letter(w):
    accum = 0
    for i in range(0,len(w)):
        accum += alpha[w[i]]
    return accum

def genTriangle(n):
    x = 0
    out = []
    for i in range(0,n):
        x += i+1
        out += [x]
    return out

T = genTriangle(100)

words = open('p042_words.txt', 'r').readlines()
words = words[0].split(",")

cnt = 0
for w in words:
    print w, word2letter(w)
    if word2letter(w) in T:
        cnt += 1

print cnt
