# Triangle is essentially a binary tree with (i, j) having
#   left children at (i+1, j) and
#   right children at (i+1, j+1)
def DFS(root, i=0, j=0):
    if i == len(root)-1:            # base case
        return root[i][j]
    
    L = traverse(root, i+1, j)      # traverse left child
    R = traverse(root, i+1, j+1)    # traverse right child
    
    return root[i][j] + max(L, R)   # back-prop up the tree with maximum value

def main(Triangle):
    max_sum = DFS(Triangle)
    print(f"the maximum total from top to bottom of the triangle:", max_sum)
    return max_sum
    
if __name__ == "__main__":
    Triangle = [
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
    # converting into list of lists
    Triangle = [[int(s) for s in l.split()] for l in Triangle]

    main(Triangle)