import numpy as np

# The key idea here is that we can iterate over every column, but we need two passes through them
#       The first pass we only go right and down
#       Then the second pass we check if going up actually produces a shorter path
def search(matrix):

    # data structures needed to solve problem
    matrix = np.array(matrix)
    path_sums = np.zeros_like(matrix)
    path_directions = np.chararray(matrix.shape)

    # base case #1: the leftmost column is forced
    path_sums[:, 0] = matrix[:, 0]
    path_directions[:, 0] = 'S'

    m, n = matrix.shape
    for j in range(1, n):

        # base case #2: the top of the columns
        path_sums[0, j] = path_sums[0, j-1] + matrix[0, j]
        path_directions[0, j] = 'R'

        # iterate down:    path_sums[i, j] = max( path_sums[i-1, j], path_sums[i, j-1] ) +  matrix[i, j]
        for i in range(1, m):
            
            path_sums[i, j] = matrix[i, j]
            if path_sums[i-1, j] < path_sums[i, j-1]:
                path_sums[i, j] += path_sums[i-1, j]
                path_directions[i, j] = 'D'
            else:
                path_sums[i, j] += path_sums[i, j-1]
                path_directions[i, j] = 'R'
        
        # iterate up:   path_sums[i, j] = max( path_sums[i, j], path_sums[i, j+1] + matrix[i, j] )
        for i in reversed(range(m-1)):
            if path_sums[i+1, j] + matrix[i, j] < path_sums[i, j]:
                path_sums[i, j] = path_sums[i+1, j] + matrix[i, j]
                path_directions[i, j] = 'U'


    """ This stuff is not needed for the final answer, but it's all the info needed to construct the actual path """
    # The index of the row that we ended at
    end_row = np.argmin(path_sums[:, -1])

    # getting path taken through matrix
    path_taken = []
    curr = (end_row, n-1)
    direction = path_directions[curr].decode("utf-8")
    while direction != 'S':
        path_taken.append(direction)
        if direction == 'D':
            curr = (curr[0]-1, curr[1])
        elif direction == 'U':
            curr = (curr[0]+1, curr[1])
        else:
            curr = (curr[0], curr[1]-1)
        direction = path_directions[curr].decode("utf-8")
    
    path_taken = list(reversed(path_taken))
    #print(path_taken)

    # index of the row that we start at
    start_row = curr[0]

    # return the solution
    return path_sums[end_row, -1]

def main(matrix):
    total = search(matrix)
    print(f"The sum of the minimal path from the left edge to right edge only going up, down, and right is:", total)
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
    
    with open("p082_matrix.txt",'r') as f:
        lines = f.readlines()
    
    matrix = [[int(x) for x in line.strip().split(',')] for line in lines]
    main(matrix)
    