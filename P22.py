names = open("p022_names.txt",'r').readlines()[0]

#this textfile is only one line, so we have to parse it into a list
names = names.split(',')
#get rid of the " "
for i in range(0,len(names)):
    names[i] = names[i][1:len(names[i])-1]

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

#sorting alphabetically
def comparison(s):
    accum = 0
    for i in range(0,len(s)):
        accum += alpha[s[i]]
    return accum

#bubble sort is too slow
"""
def alphabetical(inp):
    A = list(inp)
    k = 1
    for i in range(0, len(A)):
        for j in range(1,len(A)-i):
            while A[j-1][0:k] == A[j][0:k]:
                k += 1
            if comparison(A[j-1][0:k]) > comparison(A[j][0:k]):
                temp = A[j-1]
                A[j-1] = A[j]
                A[j] = temp
            k = 1
    return A
"""

print alphabetical(names)


for i in names:
    print i
