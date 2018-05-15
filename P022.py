names = open("p022_names.txt",'r').readlines()[0]

#this textfile is only one line, so we have to parse it into a list
names = names.split(',')
#get rid of the " "
for i in range(0,len(names)):
    names[i] = names[i][1:len(names[i])-1]

#gotta love python
names.sort()

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

def alpha_value(n):
    accum = 0
    for c in n:
        accum += alpha[c]
    return accum

accum = 0
for n in names:
    #have to up the index by 1 bc index starts at 0
    accum += (names.index(n)+1) * alpha_value(n)

print accum

#print names.index("COLIN")+1, alpha_value("COLIN")
