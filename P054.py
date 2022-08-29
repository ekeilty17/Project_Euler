from collections import Counter
import itertools

class Card(object):

    value_rank = {
        '2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8,
        '9' : 9, 'T' : 10, 'J' : 11, 'Q' : 12, 'K' : 13, 'A' : 14
    }

    def __init__(self, *args, seed=None):
        
        self.seed = seed
        if not self.seed is None:
            random.seed(self.seed)

        # some error parsing and checking
        if len(args) == 1:
            card = args[0]
            if type(card) != str or len(card) != 2:
                raise TypeError(f"Expected a string with 2 characters, got {card}")
            value = card[0]
            suit = card[1]
        
        if len(args) == 2:
            value, suit = args
            if type(value) not in [str, int] or len(str(value)) != 1:
                raise TypeError(f"In first argument, expected a single character or integer, got {value}")
            if type(suit) not in [str, int] or len(str(suit)) != 1:
                raise TypeError(f"In first argument, expected a single character or integer, got {suit}")

        self.value = str(value).upper()
        self.suit = str(suit).upper()

        if self.value not in self.all_values():
            raise ValueError(f"Got value {self.value}, expected {self.all_values()}")
        
        if self.suit not in self.all_suits():
            raise ValueError(f"Got suit {self.suit}, expected {self.all_suits()}")

    @staticmethod
    def all_values():
        return ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']

    @staticmethod
    def all_suits():
        return ['C', 'H', 'D', 'S']

    def __repr__(self):
        return f"{self.value}{self.suit}"
    

    """ When we compare cards, we only care about the value, not the suit of the card  """

    def __eq__(self, other):
        if not isinstance(other, Card):
            raise TypeError("Comparing only implemented between 'Card' types")
        return self.value == other.value
    
    def __gt__(self, other):
        if not isinstance(other, Card):
            raise TypeError("Comparing only implemented between 'Card' types")
        return self.value_rank[self.value] > self.value_rank[other.value]
    
    # only have to implement the above, and the rest follow
    def __ne__(self, other):
        return not self.__eq__(other)

    def ge(self, other):
        return self.__gt__(other) or self.__eq__(other)

    def __lt__(self, other):
        if not isinstance(other, Card):
            raise TypeError("Comparing only implemented between 'Card' types")
        return other.__gt__(self)
    
    def le(self, other):
        return self.__lt__(other) or self.__eq__(other)
        

class Hand(object):

    category_value = {
        "High Card": 0,
        "Pair": 1,
        "Two Pair": 2,
        "Three of a Kind": 3,
        "Straight": 4,
        "Flush": 5,
        "Full House": 6,
        "Four of a Kind": 7,
        "Straight Flush": 8,
        "Royal Flush": 9
    }

    def __init__(self, cards):

        self.cards = []
        for card in cards:
            if not isinstance(card, Card):
                card = Card(card)
            self.cards.append( card )
        
        # sorting to make things easier later
        self.cards = list(sorted(self.cards))
        
        # figures out what the best hand is in the list `self.card`
        # stored in `self.best` and `self.description`
        self.get_best_hand()

    def __repr__(self):
        return str(self.best) + '\t' + self.description

    """ Allows us to compare and sort hands """

    def __eq__(self, other):
        if not isinstance(other, Hand):
            raise TypeError("Comparing only implemented between 'Hand' types")
        return self.best == other.best and self.description == other.description
    
    def __gt__(self, other):
        if not isinstance(other, Hand):
            raise TypeError("Comparing only implemented between 'Hand' types")
        
        my_category = self.description.split(":")[0]
        other_category = other.description.split(":")[0]
        if my_category != other_category:
            return self.category_value[my_category] > self.category_value[other_category]
        else:
            if my_category == "Royal Flush":
                return False
            elif my_category in ["Straight Flush", "Flush", "Straight"]:
                return self.best[-1] > other.best[-1]
            elif my_category in ["Four of a Kind", "Full House", "Three of a Kind", "Pair"]:
                if self.best[0] != other.best[0]:
                    return self.best[0] > other.best[0]
                else:
                    return self.best[-1] > other.best[-1]
            elif my_category == "Two Pair":
                if self.best[0] != other.best[0]:
                    return self.best[0] > other.best[0]
                elif self.best[2] != other.best[2]:
                    return self.best[2] > other.best[2]
                else:
                    return self.best[-1] > other.best[-1]
            elif my_category == "High Card":
                for i in range(5):
                    if self.best[i] != other.best[i]:
                        return self.best[i] > other.best[i]
                return False
            else:
                raise ValueError(f"my_category got unexpected value {my_category}")
    
    # only have to implement the above, and the rest follow
    def __ne__(self, other):
        return not self.__eq__(other)

    def ge(self, other):
        return self.__gt__(other) or self.__eq__(other)

    def __lt__(self, other):
        if not isinstance(other, Hand):
            raise TypeError("Comparing only implemented between 'Hand' types")
        return other.__gt__(self)
    
    def le(self, other):
        return self.__lt__(other) or self.__eq__(other)


    """ The user methods """

    def clear_cards(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)
        self.cards = list(sorted(self.cards))
        self.get_best_hand()


    """ The internal logic to obtain best 5 cards (hand) from a set of cards of any length """

    def get_flushes(self):
        
        flushes = [] 
        for cards in self.suit_groups.values():
            if len(cards) >= 5:
                """
                # This will give you all possible flushes...but it blows up really quickly and it's kinda pointless
                for element in itertools.permutations(cards, 5):
                    flushes.append( element )
                """
                # instead I'll just return the highest flush for each suit
                flushes.append( tuple(sorted(cards))[-5:] )
        
        return flushes

    def get_straights(self):
        
        straights = []

        ordered_values = Card.all_values()
        for i in range(len(ordered_values)-4):
            for j in range(5):
                if len(self.value_groups[ ordered_values[i+j] ]) == 0:
                    break
            else:
                # if the `break` statement is never called, then the below will execute
                for straight in itertools.product(*[self.value_groups[ ordered_values[i+j] ] for j in range(5)]):
                    straights.append( tuple(sorted(straight)) )
        
        # this is because the 'A' is at the beginning of `Card.all_values()`
        # so we haven't accounted for the [T, J, Q, K, A] stright
        for value in ['T', 'J', 'Q', 'K', 'A']:
            if len(self.value_groups[value]) == 0:
                break
        else:
            # if the `break` statement is never called, then the below will execute
            for straight in itertools.product(*[self.value_groups[value] for value in ['T', 'J', 'Q', 'K', 'A']]):
                straights.append( tuple(sorted(straight)) )
        
        return straights

    # quads = four of a kind
    def get_quads(self):
        quads = []
        for cards in self.value_groups.values():
            # if it's a valid deck this should never be greater than 4
            if len(cards) == 4:
                quads.append( tuple(sorted(cards)) )

        return quads
    
    # set = three of a kind
    def get_sets(self):
        """
        Note: This is strictly sets, meaning it won't classify a four of a kind as a set
        """
        sets = []
        for cards in self.value_groups.values():
            if len(cards) == 3:
                sets.append( tuple(sorted(cards)) )
        
        return sets
    
    def get_pairs(self):
        """
        Note: This is strictly pairs, meaning it won't classify a four of a kind or a set as a pair
        """
        pairs = []
        for cards in self.value_groups.values():
            if len(cards) == 2:
                pairs.append( tuple(sorted(cards)) )
        
        return pairs


    """ This function is where all of the hard work is done """

    def get_best_hand(self):
        
        # useful data structures
        self.value_groups = { value : [] for value in Card.all_values() }
        self.suit_groups = { suit : [] for suit in Card.all_suits() }

        for card in self.cards:
            self.value_groups[card.value].append(card)
            self.suit_groups[card.suit].append(card)

        # get each category
        flushes = self.get_flushes()
        straights = self.get_straights()
        quads = self.get_quads()
        sets = self.get_sets()
        pairs = self.get_pairs()
        
        # sort them to make things easier later
        flushes = list(sorted(flushes, key=lambda cards: cards[-1]))
        straights = list(sorted(straights, key=lambda cards: cards[-1]))
        quads = list(sorted(quads, key=lambda cards: cards[-1]))
        sets = list(sorted(sets, key=lambda cards: cards[-1]))

        # checking for royal-flushes / straight-flushes
        for flush in flushes:
            for straight in straights:
                if flush == straight:
                    self.best = flush

                    if flush[-1].value == 'A':
                        self.description = "Royal Flush"
                    else:
                        self.description = f"Straight Flush: {flush[-1].value} high"
                    return self.best

        # checking for four of a kinds
        if len(quads) > 0:
            self.best = tuple( list(quads[-1]) + self.cards[-1:] )
            self.description = f"Four of a Kind: {self.best[-1].value}"

        # checking for full houses
        if len(sets) > 0:
            highest_set = sets[-1]

            highest_pair = None
            if len(sets) > 1:
                highest_pair = (sets[-2][0], sets[-2][1])
            
            if len(pairs) > 0:
                if highest_pair is None or pairs[-1][0].value > highest_pair[0].value:
                    highest_pair = pairs[-1]

            if not highest_pair is None:
                self.best = tuple( list(highest_set) + list(highest_pair) )
                self.description = f"Full House: {self.best[0].value} full of {self.best[-1].value}"
                return self.best

        # checking for flushes
        if len(flushes) > 0:
            self.best = flushes[-1]
            self.description = f"Flush: {self.best[-1].value} high"
            return self.best
        
        # checking for straights
        if len(straights) > 0:
            self.best = straights[-1]
            self.description = f"Straight: {self.best[-1].value} high"
            return self.best
        
        # checking for three of a kind
        if len(sets) > 0:
            self.best = tuple( list(sets[-1]) + self.cards[-2:] )
            self.description = f"Three of a Kind: {self.best[0].value}"
            return self.best

        # checking for two pair
        if len(pairs) > 1:
            self.best = tuple( list(pairs[-1]) + list(pairs[-2]) + self.cards[-1:] )
            self.description = f"Two Pair: {self.best[0].value} and {self.best[2].value}"
            return self.best
        
        # checking for one pair
        if len(pairs) > 0:
            self.best = tuple( list(pairs[-1]) + self.cards[-3:] )
            self.description = f"Pair: {self.best[0].value}"
            return self.best
        
        # return highest cards
        self.best = tuple(reversed(sorted( self.cards[-5:] )))
        self.description = f"High Card: {self.best[0].value}"
        return self.best


def main(Hands):
    
    P1_wins = 0
    for i, (P1, P2) in enumerate(Hands, 1):
        
        H1 = Hand(P1)
        H2 = Hand(P2)

        H1_wins = H1 > H2
        print(f"{i})\t{str(H1):60s} \t {str(H2):60s} \t P1 > P2? {H1_wins}")
        if H1_wins:
            P1_wins += 1

    print()
    print(f"The number of hands Player 1 wins:", P1_wins)
    return P1_wins

if __name__ == "__main__":
    with open('p054_poker.txt', 'r') as f:
        lines = f.readlines()

    Hands = []
    for line in lines:
        #getting each card as an element in a list
        L = line.split(" ")
        L[-1] = L[-1][0:2]

        #getting each player
        P1 = L[0:5]
        P2 = L[5:10]
        Hands.append((P1, P2))
    
    main(Hands)