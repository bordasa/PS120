import random

class Card:
    _FACE_CARD_DICT = {
        'Jack': 1,
        'Queen': 2,
        'King': 3,
        'Ace': 4
    }

    _RANK_DICT = {
        'Diamonds': 1,
        'Clubs': 2,
        'Hearts': 3,
        'Spades': 4
    }

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.face_card = not str(self.rank).isnumeric()

    def __str__(self):
        return f"{self.rank} of {self.suit}"
    
    def rank_to_num(self):
        if self.face_card:
            return (10 + Card._FACE_CARD_DICT[self.rank])
        return self.rank

    def __lt__(self, other):
        if not isinstance(other, Card):
            return NotImplemented

        if self.rank_to_num() == other.rank_to_num():
            return (Card._RANK_DICT[self.suit] 
                    < Card._RANK_DICT[other.suit])
        
        return self.rank_to_num() < other.rank_to_num()

    def __gt__(self, other):
        if not isinstance(other, Card):
            return NotImplemented

        if self.rank_to_num() == other.rank_to_num():
            return (Card._RANK_DICT[self.suit] 
                    > Card._RANK_DICT[other.suit])
        
        return self.rank_to_num() > other.rank_to_num()
    
    def __le__(self, other):
        if not isinstance(other, Card):
            return NotImplemented

        if self.rank_to_num() == other.rank_to_num():
            return (Card._RANK_DICT[self.suit] 
                    <= Card._RANK_DICT[other.suit])

        return self.rank_to_num() <= other.rank_to_num()

    def __eq__(self, other):
        if not isinstance(other, Card):
            return NotImplemented
        
        return self.rank_to_num() == other.rank_to_num() and self.suit == other.suit


class Deck:
    RANKS = list(range(2, 11)) + ['Jack', 'Queen', 'King', 'Ace']
    SUITS = ['Hearts', 'Clubs', 'Diamonds', 'Spades']

    def __init__(self):
        self._generate_deck()
    
    def _generate_deck(self):
        self.cards = []
        for suit in Deck.SUITS:
            for rank in Deck.RANKS:
                self.cards.append(Card(rank, suit))
        
        random.shuffle(self.cards)
        
        return self.cards
    
    def draw(self):
        if not self.cards:
            print("Out of cards! I will generate a new deck...")
            print("Shuffling new deck...")
            self._generate_deck()
        
        return self.cards.pop()

deck = Deck()
drawn = []
for _ in range(52):
    drawn.append(deck.draw())

count_rank_5 = sum([1 for card in drawn if card.rank == 5])
count_hearts = sum([1 for card in drawn if card.suit == 'Hearts'])

print(count_rank_5 == 4)      # True
print(count_hearts == 13)     # True

drawn2 = []
for _ in range(52):
    drawn2.append(deck.draw())

print(drawn != drawn2)        # True (Almost always).