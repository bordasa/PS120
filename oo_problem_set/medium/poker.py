# Include Card and Deck classes from the last two exercises.
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
        self.value = self.rank_to_num()

    def __str__(self):
        return f"{self.rank} of {self.suit}"
    
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, value):
        self._value = value

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

class PokerHand:
    __HAND_SIZE = 5

    def __init__(self, deck):
        self.cards = sorted([deck.draw()
                      for _ in range(PokerHand.__HAND_SIZE)])
        # self.cards = sorted(list(deck))
        self._suit_set = {card.suit for card in self.cards}
        self._value_set = {card.value for card in self.cards}
        self.count()

    def print(self):
       print("My current hand:")
       for card in self.cards:
           print(f"[{card}]")

    def count(self):
        self.value_count = {}

        for card in self.cards:
            self.value_count.setdefault(card.value, 0)
            self.value_count[card.value] += 1

    def evaluate(self):
        if self._is_royal_flush():
            return "Royal flush"
        elif self._is_straight_flush():
            return "Straight flush"
        elif self._is_four_of_a_kind():
            return "Four of a kind"
        elif self._is_full_house():
            return "Full house"
        elif self._is_flush():
            return "Flush"
        elif self._is_straight():
            return "Straight"
        elif self._is_three_of_a_kind():
            return "Three of a kind"
        elif self._is_two_pair():
            return "Two pair"
        elif self._is_pair():
            return "Pair"
        else:
          return "High card"

    def _is_royal_flush(self):
        return (self._is_straight_flush() and
                self.cards[0].value == 10)

    def _is_straight_flush(self):
        return (self._is_straight() and self._is_flush())

    def _is_four_of_a_kind(self):
        return (len(self._value_set) == 2 and
                    bool([val 
                        for val in self.value_count.values()
                        if val == 4])
                    )

    def _is_full_house(self):
        return (len(self._value_set) == 2 and
                bool([val for val in self.value_count.values()
                    if val == 3])
                    )

    def _is_flush(self):
        return len(self._suit_set) == 1

    def _is_straight(self):
        return (len(self._value_set) == 5 and 
                (self.cards[-1].value - self.cards[0].value
                     == 4))

    def _is_three_of_a_kind(self):
        return (len(self._value_set) == 3 and
            bool([val for val in self.value_count.values()
                        if val == 3]))

    def _is_two_pair(self):
        return (len(self._value_set) == 3 and
            bool([val for val in self.value_count.values()
                        if val == 2]))

    def _is_pair(self):
        return len(self._value_set) == 4
    
hand = PokerHand(Deck())
hand.print()
print(hand.evaluate())
print()

# Adding TestDeck class for testing purposes

class TestDeck(Deck):
    def __init__(self, cards):
        self.cards = cards

# All of these tests should return True

hand = PokerHand(
    TestDeck(
        [
            Card("Ace", "Hearts"),
            Card("Queen", "Hearts"),
            Card("King", "Hearts"),
            Card("Jack", "Hearts"),
            Card(10, "Hearts"),
        ]
    )
)
print(hand.evaluate() == "Royal flush")

hand = PokerHand(
    TestDeck(
        [
            Card(8, "Clubs"),
            Card(9, "Clubs"),
            Card("Queen", "Clubs"),
            Card(10, "Clubs"),
            Card("Jack", "Clubs"),
        ]
    )
)
print(hand.evaluate() == "Straight flush")

hand = PokerHand(
    TestDeck(
        [
            Card(3, "Hearts"),
            Card(3, "Clubs"),
            Card(5, "Diamonds"),
            Card(3, "Spades"),
            Card(3, "Diamonds"),
        ]
    )
)
print(hand.evaluate() == "Four of a kind")

hand = PokerHand(
    TestDeck(
        [
            Card(3, "Hearts"),
            Card(3, "Clubs"),
            Card(5, "Diamonds"),
            Card(3, "Spades"),
            Card(5, "Hearts"),
        ]
    )
)
print(hand.evaluate() == "Full house")

hand = PokerHand(
    TestDeck(
        [
            Card(10, "Hearts"),
            Card("Ace", "Hearts"),
            Card(2, "Hearts"),
            Card("King", "Hearts"),
            Card(3, "Hearts"),
        ]
    )
)
print(hand.evaluate() == "Flush")

hand = PokerHand(
    TestDeck(
        [
            Card(8, "Clubs"),
            Card(9, "Diamonds"),
            Card(10, "Clubs"),
            Card(7, "Hearts"),
            Card("Jack", "Clubs"),
        ]
    )
)
print(hand.evaluate() == "Straight")

hand = PokerHand(
    TestDeck(
        [
            Card("Queen", "Clubs"),
            Card("King", "Diamonds"),
            Card(10, "Clubs"),
            Card("Ace", "Hearts"),
            Card("Jack", "Clubs"),
        ]
    )
)
print(hand.evaluate() == "Straight")

hand = PokerHand(
    TestDeck(
        [
            Card(3, "Hearts"),
            Card(3, "Clubs"),
            Card(5, "Diamonds"),
            Card(3, "Spades"),
            Card(6, "Diamonds"),
        ]
    )
)
print(hand.evaluate() == "Three of a kind")

hand = PokerHand(
    TestDeck(
        [
            Card(9, "Hearts"),
            Card(9, "Clubs"),
            Card(5, "Diamonds"),
            Card(8, "Spades"),
            Card(5, "Hearts"),
        ]
    )
)
print(hand.evaluate() == "Two pair")

hand = PokerHand(
    TestDeck(
        [
            Card(2, "Hearts"),
            Card(9, "Clubs"),
            Card(5, "Diamonds"),
            Card(9, "Spades"),
            Card(3, "Diamonds"),
        ]
    )
)
print(hand.evaluate() == "Pair")

hand = PokerHand(
    TestDeck(
        [
            Card(2, "Hearts"),
            Card("King", "Clubs"),
            Card(5, "Diamonds"),
            Card(9, "Spades"),
            Card(3, "Diamonds"),
        ]
    )
)
print(hand.evaluate() == "High card")
