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
    
    # def __ge__(self, other):
    #     if not isinstance(other, Card):
    #         return NotImplemented

    #     return self.rank_to_num() >= other.rank_to_num()

    def __eq__(self, other):
        if not isinstance(other, Card):
            return NotImplemented
        
        return self.rank_to_num() == other.rank_to_num() and self.suit == other.suit


cards = [Card(2, 'Hearts'),
         Card(10, 'Diamonds'),
         Card('Ace', 'Clubs')]
print(min(cards) == Card(2, 'Hearts'))             # True
print(max(cards) == Card('Ace', 'Clubs'))          # True
print(str(min(cards)) == "2 of Hearts")            # True
print(str(max(cards)) == "Ace of Clubs")           # True

cards = [Card(5, 'Hearts')]
print(min(cards) == Card(5, 'Hearts'))             # True
print(max(cards) == Card(5, 'Hearts'))             # True
print(str(Card(5, 'Hearts')) == "5 of Hearts")     # True

cards = [Card(4, 'Hearts'),
         Card(4, 'Diamonds'),
         Card(10, 'Clubs')]
print(min(cards).rank == 4)                        # True
print(max(cards) == Card(10, 'Clubs'))             # True
print(str(Card(10, 'Clubs')) == "10 of Clubs")     # True

cards = [Card(7, 'Diamonds'),
         Card('Jack', 'Diamonds'),
         Card('Jack', 'Spades')]
print(min(cards) == Card(7, 'Diamonds'))           # True
print(max(cards).rank == 'Jack')                   # True
print(str(Card(7, 'Diamonds')) == "7 of Diamonds") # True

cards = [Card(8, 'Diamonds'),
         Card(8, 'Clubs'),
         Card(8, 'Spades')]
print(min(cards).rank == 8)                        # True
print(max(cards).rank == 8)                        # True