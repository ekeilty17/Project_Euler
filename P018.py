a = [
"75",
"95 64",
"17 47 82",
"18 35 87 10",
"20 04 82 47 65",
"19 01 23 75 03 34",
"88 02 77 73 07 63 67",
"99 65 04 28 06 16 70 92",
"41 41 26 56 83 40 80 70 33",
"41 48 72 33 47 32 37 16 94 29",
"53 71 44 65 25 43 91 52 97 51 14",
"70 11 33 28 77 73 17 78 39 68 17 57",
"91 71 52 38 17 14 91 43 58 50 27 29 48",
"63 66 04 68 89 53 67 30 73 16 69 87 40 31",
"04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"
]

num = []
for i in range(0,len(a)):
    temp = []
    for j in range(0,len(a[i]),3):
        temp += [int(a[i][j:j+3])]
    num += [temp]


#every path can be thought of as a 14 binary number
#   if there is a zero it means go left
#   if there is a 1 it means go right
#There are 15 lines, but the first one doesnt count since there is not decisions
#that means there are 2**14 = 16384 paths
paths = []
for i in range(0,16384):
    s = bin(i)[2:]
    if len(s) < 14:
        for j in range(len(s)-1,14):
            s = "0" + s
    paths += [s]

#the binary integer corresponds to the collumn
#if you sum the inegers together, it will tell you 
def binSum(s,n):
    accum = 0
    for i in range(0,n):
        accum += int(s[i])
    return accum


def getPath(a,bi):
    out = []
    for r in range(0,len(num)):
        out += [a[r][binSum(bi,r)]]
    return out

max_path = 0
max_path_index = 0
for i in range(0, len(paths)):
    p = getPath(num,paths[i])
    #print i, sum(p), max_path
    if sum(p) > max_path:
        print i, sum(p), max_path
        max_path = sum(p)
        max_path_index = i

print
print "Maximum Path"
print getPath(num,paths[max_path_index])
print max_path,max_path_index
print paths[max_path_index]
