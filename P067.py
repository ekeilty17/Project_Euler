def LeftChild(i, j):
    return [i+1, j]

def RightChild(i, j):
    return [i+1, j+1]

#above is the brute force solution from problem 18...too slow
#This actually physically traverses the binary tree and uses recurrsion in order to backtrack
#basically this tries every possible path, which is 2^99 iterations since that's how many paths there are
def getMaxSum_tree(root, i, j):
    print i,j
    if i == len(root)-1:
        return int(root[i][j])
    L = getMaxSum(root, i+1, j)
    R = getMaxSum(root, i+1, j+1)
    return int(root[i][j]) + max(L,R)

#The above function has the right idea, it's just slightly inefficient
#it uses the fact we know the indeces of every value, and we don't have to traverse the tree in orde to get to the bottom nor do we need to use recurrsion in order to get to the parent
#This is on the order of n^2 since there are 2 nested for loops
def getMaxSum_linebyline(root):
    for i in range(len(root)-1, 0, -1):
        for j in range(0,len(root[i])-1):
            root[i-1][j] += max(root[i][j], root[i][j+1])
        #print root[i-1]
    return root[0][0]

lines = open('p067_triangle.txt','r').readlines()
lines = [l.strip().split() for l in lines]

for i in range(0,len(lines)):
    for j in range(0,len(lines[i])):
        lines[i][j] = int(lines[i][j])

print
#print getMaxSum(lines, 0, 0)
print getMaxSum_linebyline(lines)

