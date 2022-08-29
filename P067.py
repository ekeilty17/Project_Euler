def getLeftChild(i, j):
    return i+1, j

def getRightChild(i, j):
    return i+1, j+1

# The reason this is slow is because we do a lot of repeated computation
# if two different paths hit the same node, we will do the computation at the node multiple times
def brute_force(root, i=0, j=0):
    # base-case
    if i == len(root)-1:
        return root[i][j]

    # essentially we are doing a depth-first search
    L = brute_force(root, i+1, j)
    R = brute_force(root, i+1, j+1)
    return root[i][j] + max(L, R)


# Instead, we can add the list ``max_sums`` that remembers if we've done this computation before (called memoization)
# This way if we go to a node that we've already computed, then we can just read the value
def dynamic_programming_top_down(root, max_sums=None, i=0, j=0):
    if max_sums is None:
        max_sums = [[None for _ in row] for row in Triangle]
    
    # base-case
    if i == len(root)-1:
        max_sums[i][j] = int(root[i][j])
        return max_sums[i][j]
    
    # if we haven't computed this node before, then we recursively compute it
    if max_sums[i+1][j] is None:
        max_sums[i+1][j] = dynamic_programming_top_down(root, max_sums, i+1, j)
    if max_sums[i+1][j+1] is None:
        max_sums[i+1][j+1] = dynamic_programming_top_down(root, max_sums, i+1, j+1)
    
    # get left and right child values
    L = max_sums[i+1][j]
    R = max_sums[i+1][j+1]

    # we store the result to prevent repetitive computation
    max_sums[i][j] = root[i][j] + max(L, R)
    return max_sums[i][j]


# Another method of accomplishing the same thing is to start at the bottom and work your way up to the root
# If you know the maximum sum of the left and right child, then you can determine the maximum sum of the given node
#       max_sums[i][j] = root[i][j] + max(L, R)
def dynamic_programming_bottom_up(root):
    max_sums = [[None for _ in row] for row in Triangle]

    # base case: the maximum sum of the last row is obviously just the last row
    max_sums[-1] = list(root[-1])
        
    # bottom-up recursion
    for i in reversed(range(len(root)-1)):
        for j in range(len(root[i])):
            L = max_sums[i+1][j]
            R = max_sums[i+1][j+1]
            max_sums[i][j] = root[i][j] + max(L, R)

    # we return the maximum sum of the first element
    return max_sums[0][0]


def main(Triangle):
    
    #total = brute_force(Triangle)
    #total = dynamic_programming_top_down(Triangle)
    total = dynamic_programming_bottom_up(Triangle)

    print(f"The maximum total from top to bottom in the given triangle is", total)
    return total

if __name__ == "__main__":
    # reading file
    with open('p067_triangle.txt', 'r') as f:
        lines = f.readlines()

    # putting into easy to use format (list of lists)
    Triangle = [l.strip().split() for l in lines]
    Triangle = [[int(x) for x in row] for row in Triangle]
    
    main(Triangle)