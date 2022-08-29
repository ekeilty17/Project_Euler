import copy
import numpy as np
import re

class Sudoku(object):

    offset = [  (-1, -1), (-1, 0), (-1, 1),
                (0, -1),  (0, 0),  (0, 1),
                (1, -1),  (1, 0),  (1, 1) ]

    def __init__(self, board, check_consistent=True):
        
        # some error checking
        self.board_correct_structure(board)
        self.board = np.array(board)    # will be a 9x9 numpy array

        if check_consistent:
            if not self.isConsistent():
                raise ValueError("This board contains inconsistencies")
        
        # datastructure we will use to get solution
        self.candidates = [ [self.getPossibleCellValues(r, c) for c in range(1, 10)] for r in range(1, 10) ]

    @staticmethod
    def board_correct_structure(board):
        if not type(board) in [list, np.ndarray]:
            raise TypeError("Input is not a list")
        
        if len(board) != 9:
            raise TypeError("Number of rows in input does not equal 9")

        for i in range(9):
            if len(board[i]) != 9:
                raise TypeError("Number of columns in input does not equal 9")
            for j in range(9):
                if board[i][j] not in range(10):
                    raise ValueError("Input list does not contain integers between 0 and 9 (inclusive)")

    #def __getitem__(self, index):
    #    return self.board[index]

    def __repr__(self):
        out = "\t \033[90m  -----------------------\033[0m\n"
        for i in range(9):
            temp = '\t\033[90m' + str(i+1) + ' |\033[0m '
            for j in range(9):
                if self.board[i][j] == 0:
                    temp += '  '
                else:
                    temp += str(self.board[i][j]) + ' '
                if j == 2 or j == 5:
                    temp += '\033[90m|\033[0m '
                elif j == 8:
                    temp += '\033[90m|\033[0m\n'
            out += temp
            if i == 2 or i == 5:
                out += "\t\033[90m  |-------+-------+-------|\033[0m\n"
            if i == 8:
                out += "\t\033[90m   -----------------------\033[0m\n"
        out +=  "\t \033[90m   1 2 3   4 5 6   7 8 9\033[0m\n"
        return out

    def copy(self):
        S = Sudoku( self.board.copy(), check_consistent=False )
        S.candidates = copy.deepcopy( self.candidates )
        return S

    """ basic functionality to use the Sudoku Board """

    def move(self, r, c, val):
        if not val in range(1, 10):
            raise ValueError("number {n} is out of bounds for grid with size 9")
        self.board[r-1, c-1] = val

    # Due to Sudoku convensions, when calling these functions 
    # we will index from 1 to 9 instead of 0 to 8
    def getCell(self, r, c):
        return self.board[r-1, c-1]

    def getRow(self, r):
        if r not in range(1, 10):
            raise IndexError(f"index {r} is out of bounds for grid with size 9")
        return self.board[r-1, :]

    def getCol(self, c):
        if c not in range(1, 10):
            raise IndexError(f"index {c} is out of bounds for grid with size 9")
        return self.board[:, c-1]

    # again we index from 1 to 9
    def getNeighborVals(self, r, c, include_self=False):
        r -= 1
        c -= 1
        neighbor_idx = [
            (r-1, c-1), (r-1, c), (r-1, c+1),
            (r,   c-1), (r, c),   (r, c+1),
            (r+1, c-1), (r+1, c), (r+1, c+1)
        ]
        neighbor_idx = neighbor_idx if include_self else neighbor_idx[:4] + neighbor_idx[5:]
        neighbor_idx = filter(lambda t: t[0] in range(9) and t[1] in range(9), neighbor_idx)
        
        return np.array([ self.board[idx] for idx in neighbor_idx ])

    # because these will mostly be used for iterating I thought this would be simpler
    # the 3x3 square numbers are as follows
    #       1   2   3
    #       4   5   6
    #       7   8   9
    # This will also return the values of the square in the order you would expect they would be in
    @staticmethod
    def coord2flat(r, c):
        x = (r-1) // 3
        y = (c-1) // 3
        s = 3*x + y
        return s+1
    
    @staticmethod
    def flat2coord(s):
        x = (s-1) // 3
        y = (s-1) % 3
        r = 2 + 3*x
        c = 2 + 3*y
        return r, c
    
    def getSquare(self, s):
        if s not in range(1, 10):
            raise IndexError(f"index {s} is out of bounds for grid with size 9")

        r, c = self.flat2coord(s)
        return self.getNeighborVals(r, c, include_self=True)

    def getSquareIndexes(self, s, include_self=True):
        r, c = self.flat2coord(s)
        idx = [
            (r-1, c-1), (r-1, c), (r-1, c+1),
            (r,   c-1), (r, c),   (r, c+1),
            (r+1, c-1), (r+1, c), (r+1, c+1)
        ]

        return np.array(idx) if include_self else np.array(idx[:4] + idx[5:])

    # returns values from top left to bottom right
    def getDiagonal(self, k=0):
        return np.diag(self.board, k)
    
    # returns values from bottom left to top right
    def getSkewDiagonal(self, k=0):
        return np.flip(np.diag(np.flip(self.board, axis=1), k))

    """ functionality related to solving the Sudoku """
    def getPossibleCellValues(self, r, c):
        if self.getCell(r, c) != 0:
            return set([self.getCell(r, c)])

        row = self.getRow(r)
        col = self.getCol(c)
        square = self.getSquare(self.coord2flat(r, c))
        not_possible_values = set(np.concatenate((row, col, square)))
        
        return set(range(1, 10)) - not_possible_values

    def get_most_restructed_cells(self):
        
        flat = [ (x+1, y+1, self.candidates[x][y]) for y in range(9) for x in range(9) if self.board[x][y] == 0]
        sorted_flat = list(sorted(flat, key=lambda t: len(t[2])))

        return sorted_flat#[(r, c) for r, c, _ in sorted_flat]

    def update_candidates(self, r, c, val):
        x, y = r-1, c-1
        self.candidates[x][y] = set([val])

        # remove candidate from rows
        for i in range(1, 10):
            if i == r:
                continue
            self.candidates[i-1][y] = self.candidates[i-1][y] - self.candidates[x][y]

        # remove candidate from cols
        for j in range(1, 10):
            if j == c:
                continue
            self.candidates[x][j-1] = self.candidates[x][j-1] - self.candidates[x][y]

        # remove candidate from square
        s = self.coord2flat(r, c)
        for i, j in self.getSquareIndexes(s, include_self=True):
            if i == r and j == c:
                continue
            self.candidates[i-1][j-1] = self.candidates[i-1][j-1] - self.candidates[x][y]

    """ Verfication of solution """
    def isComplete(self):
        return not np.any(self.board == 0)
    
    @staticmethod
    def hasRepeats(L):
        return list(sorted(L)) != list(sorted(set(L)))

    # This might not be super efficient, but it's only a 9x9 board
    def isConsistent(self, diagonals=False):
        for i in range(1, 10):
            row = list(filter(lambda x: x != 0, self.getRow(i)))
            col = list(filter(lambda x: x != 0, self.getCol(i)))
            square = list(filter(lambda x: x != 0, self.getSquare(i)))
            if self.hasRepeats(row) or self.hasRepeats(col) or self.hasRepeats(square):
                return False
        
        if diagonals:
            diagonal = list(filter(lambda x: x != 0, self.getDiagonal()))
            skew_diagonal = list(filter(lambda x: x != 0, self.getSkewDiagonal()))
            if self.hasRepeats(diagonal) or self.hasRepeats(skew_diagonal):
                return False
        
        return True

    def isSolution(self):
        return self.isComplete() and self.isConsistent()

    """ Solving the Sudoku """
    # also sometimes called "Soul Candidate"
    def nakedSingles(self):
        '''cell only has 1 candidate''' 
        naked_singles = [(r, c, candidates) for r, c, candidates in self.get_most_restructed_cells() if len(candidates) == 1]
        for r, c, candidates in naked_singles:
            val = candidates.pop()
            self.move(r, c, val)
            #self.update_candidates(r, c, val)
        
        self.candidates = [ [self.getPossibleCellValues(r, c) for c in range(1, 10)] for r in range(1, 10) ]
        return naked_singles != []


    def uniqueCandidate(self):
        '''value appears in only 1 cell of a square'''
        changed = False
        for s in range(1, 10):
            
            inverted_index = [set([]) for _ in range(1, 10)]
            for r, c in self.getSquareIndexes(s, include_self=True):
                for val in self.candidates[r-1][c-1]:
                    inverted_index[val-1].add((r, c))
            
            for val in range(1, 10):
                if len(inverted_index[val-1]) == 1:
                    r, c = inverted_index[val-1].pop()
                    if self.board[r-1][c-1] != 0:
                        continue
                    self.move(r, c, val)
                    #self.update_candidates(r, c, val)
                    changed = True
        
        for r in range(1, 10):
            inverted_index = [set([]) for _ in range(1, 10)]
            for j in range(1, 10):
                for val in self.candidates[r-1][j-1]:
                    inverted_index[val-1].add((r, j))
            
            for val in range(1, 10):
                if len(inverted_index[val-1]) == 1:
                    r, c = inverted_index[val-1].pop()
                    if self.board[r-1][c-1] != 0:
                        continue
                    self.move(r, c, val)
                    #self.update_candidates(r, c, val)
                    changed = True
        
        for c in range(1, 10):
            inverted_index = [set([]) for _ in range(1, 10)]
            for i in range(1, 10):
                for val in self.candidates[i-1][c-1]:
                    inverted_index[val-1].add((i, c))
            
            for val in range(1, 10):
                if len(inverted_index[val-1]) == 1:
                    r, c = inverted_index[val-1].pop()
                    if self.board[r-1][c-1] != 0:
                        continue
                    self.move(r, c, val)
                    #self.update_candidates(r, c, val)
                    changed = True

        self.candidates = [ [self.getPossibleCellValues(r, c) for c in range(1, 10)] for r in range(1, 10) ]
        return changed
    
    def logical_step(self):
        """
        changing = True
        while changing:
            changing1 = self.nakedSingles()
            #print(self)
            changing2 = self.uniqueCandidate()
            #print(self)
            changing = changing1 or changing2
        """
        changing1 = self.nakedSingles()
        changing2 = self.uniqueCandidate()
        return changing1 or changing2


class SudokuSearchTree(object):

    def __init__(self, x):
        self.val = x
        self.children = []
        self.parent = None

    def AddSuccessor(self, T):
        self.children += [T]
        T.parent = self
        return T

    """ Helper Methods """
    # Some are optional and some the user MUST define an implementation

    def isSolution(self):
        return self.val.isSolution()

    def prune(self):
        if not self.val.isConsistent():
            return True
        
        for row in self.val.candidates:
            if set() in row:
                return True
            if set.union(*row) != set(range(1, 10)):
                return True

        for c in range(1, 10):
            col = [self.val.candidates[i][c-1] for i in range(9)]
            if set.union(*col) != set(range(1, 10)):
                return True

        for s in range(1, 10):
            square = [self.val.candidates[r-1][c-1] for r, c in self.val.getSquareIndexes(s, include_self=True)]
            if set.union(*square) != set(range(1, 10)):
                return True

        return False

    def getEdges(self):
        cells = self.val.get_most_restructed_cells()

        # I actually only need to look at the most restricted cell, because we know one of them has to be correct
        r, c, candidates = cells[0]
        return [ (r, c, val) for val in candidates ]

    def heuristic(self, L):
        # edges are already sorted by least number of candidates
        return L

    def copy_node(self):
        S = SudokuSearchTree( self.val.copy() )
        return S

    def evolve(self, E):
        r, c, val = E
        self.val.move(r, c, val)
        #self.val.update_candidates(r, c, val)
        self.val.candidates = [ [self.val.getPossibleCellValues(r, c) for c in range(1, 10)] for r in range(1, 10) ]
        return self

    def __repr(self):
        return self.val.__repr__()

    def search(self):
        # If a node is not properly defined
        # of if we get to the end of the search tree
        if self == None:
            return False


        # Display Node. This is optional.
        #print(self.val)
        #print(self.val.candidates)

        # Break case...solution found
        if self.isSolution():
            return self

        # Prune the path and stop if it proves to be futile
        if self.prune():
            return False

        changing = True
        while changing:

            changing = self.val.logical_step()

            if self.prune():
                return False
        
        if self.isSolution():
            return self

        #print(self.val)
        #print(self.val.candidates)

        # Getting set of next possible states
        # Edges is a list of all possible Edges
        #   Edges take the parent node to the child node
        #   For example if the game was chess, an edge would be moving a pawn from a2 to a4
        #   and the evolve function is responsible for handling that logic
        # child = evolve(parent, Edges[i])
        Edges = self.getEdges()

        # Since this is a depth first search rather than breadth first,
        # we are looking at one child at a time rather than all children
        # so if we have some type of heuristic to order which child we should look at
        # it can dramatically improve the time of the search
        Edges = self.heuristic(Edges)

        for E in Edges:
            #print("\n\nBranching on", E)
            # creating child
            #   copy.deepcopy() creates a copy of the current node
            #   evolve(parent, E) updates the state of the node to the next state based on the edge
            child = self.AddSuccessor( self.copy_node().evolve(E) )

            # searching
            r = child.search()
            if r != False:
                # back propogating if we have found a solution
                return r
        return False

def main(boards):

    solved_boards = []
    for i, board in enumerate(boards, 1):
        print("Grid:", i)
        
        S = Sudoku(board)
        print(S)

        T = SudokuSearchTree(S)
        leaf = T.search()
        if leaf == False:
            print("Could not find solution")
            raise Exception("could not solve board at index", i)
        else:
            print(leaf.val)
            print("Solution Found!")
            print(leaf.val.board[0][0:3])
            solved_boards.append(leaf.val)

        print("\n", "-"*50)


    # getting project euler solution
    total = 0
    for S in solved_boards:
        total += int( str(S.board[0][0]) + str(S.board[0][1]) + str(S.board[0][2]) )

    print(f"The sum of the 3-digit numbers found in the top left corner of each solution grid is:", total)
    return total


if __name__ == "__main__":
    # loading data
    with open("p096_sudoku.txt", 'r') as f:
        contents = f.read()
    
    # formatting input
    boards = re.split('Grid \d\d\\n', contents)[1:]
    boards = [
        [[int(x) for x in row] for row in board.split('\n') if row != '']
    for board in boards ]
    boards = [np.array(board) for board in boards]

    # calling main function
    main(boards)