# preparing the matrix to make it usable
f=open("p081_matrix.txt",'r')

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

M = small_matrix

paths = []
for i in range(len(M)):
    temp = []
    for j in range(len(M)):
        temp += [[]]
    paths += [temp]
paths[-1][-1] = [M[-1][-1]]

dirs = []
for i in range(len(M)):
    temp = []
    for j in range(len(M)):
        temp += [[]]
    dirs += [temp]
dirs[0][0] = ['START']
dirs[-1][-1] = ['DONE']

# The trick is you don't need to know the actual path, you just need to know the minimum sum
# So we can easily compute the minimum sum at every cell
#       The bottom row and left column are forced
#       Every other cell will simply be the min(cell below, cell right)
#       We start at the bottom right cell and work out way backwards

for i in range(len(M)-2, -1, -1):
    # bottom row
    paths[-1][i] += [M[-1][i]] + paths[-1][i+1]
    dirs[-1][i] += ['R'] + dirs[-1][i+1]
    M[-1][i] += M[-1][i+1]
    # right column
    paths[i][-1] += [M[i][-1]] + paths[i+1][-1]
    dirs[i][-1] += ['D'] + dirs[i+1][-1]
    M[i][-1] += M[i+1][-1]
    
for r in range(len(M)-2, -1, -1):
    for c in range(len(M)-2, -1, -1):
        # min sum at cell = cell value + min(cell value below, cell value right)
        if M[r][c+1] < M[r+1][c]:
            paths[r][c] += [M[r][c]] + paths[r][c+1]
            dirs[r][c] += ['R'] + dirs[r][c+1]
            M[r][c] += M[r][c+1]
        else:
            paths[r][c] += [M[r][c]] + paths[r+1][c]
            dirs[r][c] += ['D'] + dirs[r+1][c]
            M[r][c] += M[r+1][c]
        #M[r][c] += min(M[r][c+1], M[r+1][c])

print paths[0][0]
print dirs[0][0]
print M[0][0]
