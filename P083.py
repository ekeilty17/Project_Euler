import numpy as np

# Need to implement something like Dijkstra's Algorithm
def getNeighbors(pos, shape):
    r, c = pos
    m, n = shape
    possible_neighbors = [ (r-1, c), (r, c-1), (r, c+1), (r+1, c) ]
    neighbors_in_range = list(filter(lambda t: 0 <= t[0] < m and 0 <= t[1] < n, possible_neighbors))
    return neighbors_in_range

def direction(u, v):
    if u[0] == v[0] and u[1] == v[1]+1:
        return 'L'
    elif u[0] == v[0] and u[1] == v[1]-1:
        return 'R'
    elif u[0] == v[0]+1 and u[1] == v[1]:
        return 'U'
    elif u[0] == v[0]-1 and u[1] == v[1]:
        return 'D'
    else:
        return 'N'

def relax(dist, path, M, u, v):
    if dist[v] > dist[u] + M[v]:
        dist[v] = dist[u] + M[v]
        path[v] = direction(u, v)
    
    return dist, path


# This implementation of Dijkstra uses a sorted list as the priority queue
# So it is O(V^2) = O((m*n)^2) complexity
# We could get more efficient using a priority queue, but I'd have to implement it from scratch 
# due to the decrease queue functionality that is needed
def Dijkstra(M, start):
    M = np.array(M)
    m, n = M.shape

    # data structures needed to solve problem
    dist = np.ones_like(M) * np.inf
    path = np.chararray(M.shape)

    # Initializing data structures
    dist[start] = M[start]
    path[:, :] = 'N'            # 'N' = None
    path[start] = 'S'           # 'S' = start

    # Q is a priority queue implemented as a sorted list (according to the dist array)
    # visited is a helper for the priority queue
    Q = [start]
    visited = np.zeros_like(M, dtype=int)
    
    while len(Q) != 0:
        
        # extracting minimum, which is always the first element
        u = Q[0]
        Q = Q[1:]
        visited[u] = 1

        # getting all unvisited neighbors of u
        neighbors = getNeighbors(u, (m, n))
        unvisited_neighbors = list(filter(lambda t: not visited[t], neighbors))
        sorted_unvisited_neighbors = list(sorted(unvisited_neighbors, key=lambda t: M[t]))

        # we relax all neighbors we have not visited yet
        for v in sorted_unvisited_neighbors:
            # relaxing node v
            if dist[v] > dist[u] + M[v]:
                dist[v] = dist[u] + M[v]
                path[v] = direction(u, v)

                # updating priority queue, which means putting v into the correct index to keep Q sorted by dist
                Q = [v] + Q
                for k in range(len(Q)-1):
                    if dist[Q[k]] > dist[Q[k+1]]:
                        Q[k], Q[k+1] = Q[k+1], Q[k]
                    else:
                        break

    return dist, path


# Now this is just a shortest path problem
# There are two standard shorteset path algorithms: Bellman-Ford and Dijkstra
#       Bellman-Ford is O(V*E), but since the matrix is a grid, E = O(V), so it's less efficient than Dijstra
#       Dijkstra we can theoretically get to O(E lg V) or O(V lg V)
def shortest_path(matrix):
    matrix = np.array(matrix)
    dist, path = Dijkstra(matrix, (0, 0))

    """ This stuff is not needed for the final answer, but it's all the info needed to construct the actual path """
    # getting path taken through matrix
    path_taken = []
    m, n = matrix.shape
    curr = (m-1, n-1)
    direction = path[curr].decode("utf-8")
    while direction != 'S':
        path_taken.append(direction)
        if direction == 'D':
            curr = (curr[0]-1, curr[1])
        elif direction == 'U':
            curr = (curr[0]+1, curr[1])
        elif direction == 'R':
            curr = (curr[0], curr[1]-1)
        else:
            curr = (curr[0], curr[1]+1)
        direction = path[curr].decode("utf-8")
    
    path_taken = list(reversed(path_taken))
    #print(path_taken)

    return int(dist[-1, -1])

def main(matrix):
    total = shortest_path(matrix)
    print(f"The shortest path from the top left to the bottom right is:", total)
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
    
    with open("p083_matrix.txt",'r') as f:
        lines = f.readlines()
    
    matrix = [[int(x) for x in line.strip().split(',')] for line in lines]
    main(matrix)
    
    
    