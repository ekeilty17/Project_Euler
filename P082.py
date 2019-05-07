# preparing the matrix to make it usable
f=open("p082_matrix.txt",'r')

matrix = []
lines = f.readlines()
for line in lines:
   matrix += [line.split('\n')[0].split(',')]

f.close()

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        matrix[i][j] = int(matrix[i][j])

small_matrix = [    [131, 673, 234, 103,  18],
                    [201,  96, 342, 965, 150],
                    [630, 803, 746, 422, 111],
                    [537, 699, 497, 121, 956],
                    [805, 732, 524,  37, 331]]

small_small_matrix = [  [100, 100, 100,  11,  12],
                        [  1,   2, 100,  10, 100],
                        [100,   3, 100,   9, 100],
                        [100,   4, 100,   8, 100],
                        [100,   5,   6,   7, 100]]

M = matrix

# copying M
original = [x[:] for x in M]

paths = []
for i in range(len(M)):
    temp = []
    for j in range(len(M)):
        temp += [[]]
    paths += [temp]
for r in range(len(paths)):
    paths[r][-1] = [M[r][-1]]

dirs = []
for i in range(len(M)):
    temp = []
    for j in range(len(M)):
        temp += [[]]
    dirs += [temp]

# Using a similar method as the previous problem
#   We solve this column by column
#       The right column is a given
#       For each subsequent column, we need to determine the row that contains the shortest path to the previous column
#           We start at the top and initialize with just going straight to the right
#           Then we iterate down the rows and determine min(moving up, moving right)
#           Then we iterate up the rows and determine min(moving down, previously determined path)

for c in range(len(M[0])-2, -1, -1):
    
    M[0][c] += M[0][c+1]
    paths[0][c] = [original[0][c]] +  paths[0][c+1]
    dirs[0][c] = ['R'] + dirs[0][c+1]
    
    # iterate down
    for r in range(1, len(M)):
        # min(moving up, moving right)
        if M[r-1][c] < M[r][c+1]:
            M[r][c] += M[r-1][c]
            paths[r][c] = [original[r][c]] + paths[r-1][c]
            dirs[r][c] = ['U'] + dirs[r-1][c]
        else:
            M[r][c] += M[r][c+1]
            paths[r][c] = [original[r][c]] + paths[r][c+1]
            dirs[r][c] = ['R'] + dirs[r][c+1]
    
    # iterate up
    for r in range(len(M)-2, -1, -1):
        # min(moving down, previously determined path)
        if M[r+1][c] + original[r][c] < M[r][c]:
            M[r][c] = original[r][c] + M[r+1][c]
            paths[r][c] = [original[r][c]] + paths[r+1][c]
            dirs[r][c] = ['D'] + dirs[r+1][c]

"""
for r in M:
    print r
print
"""
col0 = [r[0] for r in M]
print paths[col0.index(min(col0))][0]
print dirs[col0.index(min(col0))][0]
print min(col0)
print

