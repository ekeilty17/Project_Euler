import numpy as np

# This is a dynamic programming-esque solution
def search(matrix):

    # data structures needed to solve problem
    matrix = np.array(matrix)
    path_sums = np.zeros_like(matrix)
    path_directions = np.chararray(matrix.shape)
    
    # base case #1: first cell
    path_sums[0, 0] = matrix[0, 0]
    path_directions[0, 0] = 'S'

    # base case #2: we notice that the leftmost column and top row are forced
    m, n = matrix.shape
    for i in range(1, m):
        path_sums[i, 0] = path_sums[i-1, 0] + matrix[i, 0]      # leftmost column
        path_directions[i, 0] = 'D'
    for j in range(1, n):
        path_sums[0, j] = path_sums[0, j-1] + matrix[0, j]      # top row
        path_directions[0, j] = 'R'

    # Now for the recurrsion
    # with the given base-cases, the recusion for each cell becomes
    #       path_sums[i, j] = min(path_sums[i-1, j], path_sums[i, j-1]) + matrix[i, j]
    # we can accomplish this by iterating from left to right, top to bottom
    for i in range(1, m):
        for j in range(1, n):
            path_sums[i, j] = matrix[i, j]
            if path_sums[i-1, j] < path_sums[i, j-1]:
                path_sums[i, j] += path_sums[i-1, j]
                path_directions[i, j] = 'D'
            else:
                path_sums[i, j] += path_sums[i, j-1]
                path_directions[i, j] = 'R'


    """ This stuff is not needed for the final answer, but it's all the info needed to construct the actual path """
    # getting path taken through matrix
    path_taken = []
    curr = (m-1, n-1)
    direction = path_directions[curr].decode("utf-8")
    while direction != 'S':
        path_taken.append(direction)
        if direction == 'D':
            curr = (curr[0]-1, curr[1])
        else:
            curr = (curr[0], curr[1]-1)
        direction = path_directions[curr].decode("utf-8")
    
    path_taken = list(reversed(path_taken))
    #print(path_taken)

    # return the solution
    return path_sums[-1, -1]

def main(matrix):
    total = search(matrix)
    print(f"The sum of the minimal path from the top left to the bottom right only going down and right is:", total)
    return total

if __name__ == "__main__":
    """
    # testing matrix
    small_matrix = [    [131, 673, 234, 103,  18],
                        [201,  96, 342, 965, 150],
                        [630, 803, 746, 422, 111],
                        [537, 699, 497, 121, 956],
                        [805, 732, 524,  37, 331]]
    main(small_matrix)
    """
    
    with open("p081_matrix.txt",'r') as f:
        lines = f.readlines()
    
    matrix = [[int(x) for x in line.strip().split(',')] for line in lines]
    main(matrix)