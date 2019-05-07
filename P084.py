from random import randint, sample

# This is called a Monte Carlo solution 
#   Instead of tediously working out probabilities, we just use randomness to simulate the result

# Game Object Classes
class Dice:
    
    def __init__(self, sides):
        self.sides = sides
        self.val = randint(1, self.sides)

    def roll(self):
        self.val = randint(1, self.sides)
        return self.val

    def __str__(self):
        return str(self.val)
    
    def __eq__(self, D):
        if isinstance(D, Dice):
            return self.val == D.val
        if isinstance(D, int):
            return self.val == D

    def __add__(self, D):
        if isinstance(D, Dice):
            return self.val + D.val
        if isinstance(D, int):
            return self.val + D

class Deck:

    def __init__(self, cards):
        self.cards = cards

    def shuffle(self):
        self.cards = sample(self.cards,len(self.cards))

    def draw(self):
        self.cards = self.cards[1:] + [self.cards[0]]
        return self.cards[-1]

    def __len__(self):
        return len(self.cards)

    def __getitem__(self, index):
        return self.cards[index]
    
    def __str__(self):
        return str(self.cards)

# Initializing Game
squares = [ "GO",   "A1", "CC1", "A2",  "T1", "R1", "B1",  "CH1", "B2", "B3", 
            "JAIL", "C1", "U1",  "C2",  "C3", "R2", "D1",  "CC2", "D2", "D3",
            "FP",   "E1", "CH2", "E2",  "E3", "R3", "F1",  "F2",  "U2", "F3",
            "G2J",  "G1", "G2",  "CC3", "G3", "R4", "CH3", "H1",  "T2", "H2"]

CC = Deck([ "GO", "JAIL", "0", "0", "0", "0", "0", "0", 
            "0",  "0",    "0", "0", "0", "0", "0", "0"])
CH = Deck([ "GO", "JAIL", "C1", "E3", "H2", "R1", "R", "R", 
            "U",  "3",    "0",  "0",  "0",  "0",  "0", "0"])

CC.shuffle()
CH.shuffle()

sides = 4           # variable Project Euler wants to toggle
D1 = Dice(sides)
D2 = Dice(sides)


# Game Functions
def nextR(pos):
    for i in range(len(squares)):
        if squares[(pos + i+1)%len(squares)][0] == "R":
            return (pos + i+1)%len(squares)

def nextU(pos):
    for i in range(len(squares)):
        if squares[(pos + i+1)%len(squares)][0] == "U":
            return (pos + i+1)%len(squares)

def goto(s):
    return squares.index(s)

def action(curr):
    
    # land on Go to Jail square
    if squares[curr] == "G2J":
        return goto("JAIL")
    
    # Land on Community Chest Square
    if squares[curr][:2] == "CC":
        card = CC.draw()
        if card in ["GO", "JAIL"]:
            return goto(card)
        return curr
    
    # Land on Chance Square
    if squares[curr][:2] == "CH":
        card = CH.draw()
        if card in ["GO", "JAIL", "C1", "E3", "H2", "R1"]:
            return goto(card)
        if card == "R":
            return nextR(curr)
        if card == "U":
            return nextU(curr)
        if card == "3":
            return action( (curr - 3)%len(squares) )
        return curr
    
    return curr


# List to keep track of number of times each square was visitied
visited = [0]*len(squares)
doubles = 0
curr = 0

# Number of turns in the simulation
N = 5000000         # This is what it needs to be in order to give consistent results
for i in range(N):
    
    # rolling dice
    D = D1.roll() + D2.roll()
    # accounting for doubles
    if D1 == D2:
        doubles += 1
    else:
        doubles = 0
    # if 3 consecutive doubles then go straight to jail
    if doubles == 3:
        curr = goto("JAIL")
        doubles = 0
    # otherwise move to new square
    else:
        curr += D
        curr %= len(squares)    # because we loop around the board
    
    # applying rules of that square
    curr = action(curr)
    # updating visited list 
    #   (we only care about where the player is at the end of their turn, 
    #    don't care about any intermediate squares they visit)
    visited[curr] += 1
    
outcomes = [(x/float(sum(visited)))*100 for x in visited]

sorted_squares = list(reversed(sorted(squares, key=lambda x: outcomes[squares.index(x)])))
outcomes = list(reversed(sorted(outcomes)))

print
for i in range(len(outcomes)):
    print sorted_squares[i], outcomes[i]
print

modal = int( str(squares.index(sorted_squares[0])) + str(squares.index(sorted_squares[1])) + str(squares.index(sorted_squares[2])) )
print modal
