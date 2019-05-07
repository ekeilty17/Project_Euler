# preparing the matrix to make it usable
f=open("p083_matrix.txt",'r')

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

small_small_matrix = [  [  1,   2,   3,   4, 100],
                        [100, 100, 100,   5, 100],
                        [  9,   8,   7,   6, 100],
                        [ 10, 100, 100, 100, 100],
                        [ 11,  12,  13,  14,  15]]

M = matrix

# Need to implement something like Dijkstra's Algorithm
def getNeighbors(pos):
    r = pos[0]
    c = pos[1]
    out = [ [r-1, c], [r, c-1], [r, c+1], [r+1, c] ]
    out = list(filter(lambda x: 0 <= x[0] < len(M) and 0 <= x[1] < len(M), out))
    return out

def Dijkstra(M, start):
    
    # Initialize all dists as infinite
    dist = [[-1]*len(M[0]) for i in range(len(M))]
    # Initialize all paths as undefined
    path = [[[]]*len(M[0]) for i in range(len(M))]
    # Create a vertex set initialized with all verteces
    Q = [ [i,j] for i in range(len(M)) for j in range(len(M[0])) ]
    # This is technically not necessary, but significantly speeds things up
    visited = [[False]*len(M[0]) for i in range(len(M))]
    
    # First distance is given
    dist[start[0]][start[1]] = M[start[0]][start[1]]
    path[start[0]][start[1]] = [M[start[0]][start[1]]]

    while len(Q) != 0:
        
        print len(Q)
        
        # Find vertex with min distance to previous node and remove it
        u = []        
        min_dist = -1
        for i in range(len(dist)):
            for j in range(len(dist[i])):
                if dist[i][j] == -1 or visited[i][j]:
                    continue
                if u == []:
                    u = [i, j]
                    min_dist = dist[i][j]
                elif dist[i][j] < min_dist:
                    u = [i, j]
                    min_dist = dist[i][j]
        Q.remove(u)
        visited[u[0]][u[1]] = True
        
        Neighbors = getNeighbors(u)
        Neighbors = list(filter(lambda x: x in Q, Neighbors))
        Neighbors = list(sorted(Neighbors, key=lambda x: M[x[0]][x[1]]))

        for v in Neighbors:
            if not visited[v[0]][v[1]]:
                # if current path shorter than previous path (remember -1 = inf)
                if ( dist[v[0]][v[1]] == -1 ) or ( dist[u[0]][u[1]] + M[v[0]][v[1]] < dist[v[0]][v[1]]) :
                    dist[v[0]][v[1]] = dist[u[0]][u[1]] + M[v[0]][v[1]]
                    path[v[0]][v[1]] = path[u[0]][u[1]] + [M[v[0]][v[1]]]
    return [dist, path]

[dist, path] = Dijkstra(M, [0,0])

"""
print
for d in dist:
    print d
print
for p in path:
    print p
print
"""
print
print path[-1][-1]
print
print dist[-1][-1]
print
