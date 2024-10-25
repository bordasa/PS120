import random
import os

def clear_screen():
    os.system("clear")

def pause():
    input("Press <Enter> to continue.\n")

class Card:
    def __init__(self, name, value, suit):
        self.name = name
        self.value = value
        self.suit = suit

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, value):
        self._value = value
    
    @property
    def suit(self):
        return self._suit
    
    @suit.setter
    def suit(self, suit):
        self._suit = suit

    def __str__(self):
        return f"[{self.name.title()} of {self.suit.title()}]"


class Deck:
    def __init__(self):
        self._suits = ['spades', 'hearts', 'diamonds', 'clubs']
        # self.names = ['one', 'two', 'three', 'four',
        #               'five', 'six', 'seven', 'eight',
        #               'nine', 'ten', 'jack', 'queen',
        #               'king', 'ace',]
        self._name_value_dict = {
            'two': 2,
            'three': 3,
            'four': 4,
            'five': 5,
            'six': 6,
            'seven': 7,
            'eight': 8,
            'nine': 9,
            'ten': 10,
            'jack': 10,
            'queen': 10,
            'king': 10,
            'ace': 11,
        }
        self._cards = self.reset()
        self._count = len(self.cards)

    def reset(self):
        self.cards = []
        for suit in self._suits:
            for name, value in self._name_value_dict.items():
                self.cards.append(Card(name, value, suit))
                
        random.shuffle(self.cards)
        print("All of the cards are thoroughly shuffled.")

        return self.cards

    # def deal(self):
    #     pass

class Participant:
    def __init__(self):
        self._hand = []
        self._score = 0
        self._aces = 0
    
    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, score):
        self._score = score

    @property
    def aces(self):
        return self._aces
    
    @aces.setter
    def aces(self, aces):
        self._aces = aces

    def hit(self, deck):
        new_card = deck._cards.pop(0)
        self._hand.append(new_card)
        self._score += new_card.value

        if new_card.name == 'ace':
            self._aces += 1

    # def stay(self):
    #     pass

    def is_busted(self):
        return self.score > TwentyOneGame._GAME_GOAL

    def update_score(self):

        while self.is_busted() and self.aces > 0:
            print(f"Current Score is {self.score}.")
            print(f"That is greater than {TwentyOneGame._GAME_GOAL}.")
            print("The Ace must convert from 11 to 1.")
            self.aces -= 1
            self.score -= 10
            input("Press <Enter> to continue.\n")
    
    def show_hand(self):
        print(f"{self.__class__.__name__} has:")
        for card in self._hand:
            print(card)
        print()
    
    def display_score(self):
        print(f"{self.__class__.__name__} Score: {self.score}")
    
    def discard_hand(self):
        print(f"{self.__class__.__name__} adds {len(self._hand)}"
              " to the discard pile.")
        self._hand = []
        self.score = 0
        self.aces = 0
        
class Player(Participant):
    def __init__(self):
        super().__init__()
        self._dollars = TwentyOneGame._STARTING_DOLLARS
    
    def out_of_money(self):
        return self._dollars == 0
    
    def display_dollars(self):
        print(f"Player has ${self._dollars}.")

class Dealer(Participant):
    _THRESHOLD = 17

    def __init__(self):
        super().__init__()

    def show_one_card(self):
        first_card = self._hand[0]
        print("The Dealer flips one card to reveal:")
        print(f"{first_card}")
        print(f"Dealer Score: {first_card.value}")
        pause()

class TwentyOneGame:

    _GAME_GOAL = 21
    _STARTING_HAND_SIZE = 2
    _DECK_THRESHOLD = 40
    _STARTING_DOLLARS = 5
    _ANTE = 1
    _WINNING_THRESHOLD = 10

    def __init__(self):
        self.player = Player()
        self.dealer = Dealer()
        self._deck = Deck()
        self.reset_winnings()

    def start(self):

        self.display_welcome_message()

        while True:
            clear_screen()
            self.deal_cards()
            self.player_turn()
            self.dealer_turn()
            self.display_result()

            if (self.player_wins_too_much()
                or self.player_bankrupt()
                or not self.play_again()
                ):
                break

            print()
            self.player.discard_hand()
            self.dealer.discard_hand()
            self.reshuffle_deck()
            self.reset_winnings()

        self.display_goodbye_message()
    
    def player_wins_too_much(self):
        if self.player._dollars >= TwentyOneGame._WINNING_THRESHOLD:
            self.player.display_dollars()
            print("You win too much! Get out of here!")
            print()
            return True
        return False

    def player_bankrupt(self):
        if self.player.out_of_money():
            print("You are bankrupt! Game over.")
            return True
        return False

    def reset_winnings(self):
        self._winnings = TwentyOneGame._ANTE

    def ante_up(self):
        print(f"The minimum bet is ${TwentyOneGame._ANTE}.")

        if self.player._dollars >= TwentyOneGame._ANTE:
            self.player._dollars -= TwentyOneGame._ANTE
        else:
            self._winnings = self.player._dollars
            self.player._dollars = 0

        self.player.display_dollars()
        
        while True:
            print("Would you like to raise the stakes?")
            print("-1: [Y]es")
            print("-2: [N]o")
            raise_the_stakes = input()
    
            if raise_the_stakes.lower() in ['1', 'y']:
                self.take_bet()
                self.display_current_bet()
                break
            elif raise_the_stakes.lower() in ['2', 'n']:
                self.display_current_bet()
                break
            
            print("Invalid input. Please select '1' or '2'.")

    def display_current_bet(self):
        print(f"Your bet is currently ${self._winnings}.")
        pause()

    def take_bet(self):
        while True:
            print(f'Player has: ${self.player._dollars}')
            if self.player._dollars <= 0:
                print("You cannot place a bet.")
                break
            print("All winnings will be doubled.")
            print('How much would you like add to the pot?')
            bet = input()

            if bet.isnumeric():
                bet = int(bet)
                if bet <= self.player._dollars:
                    self._winnings += bet
                    self.player._dollars -= bet
                    break
                else:
                    print(f"Your bet must be ${self.player._dollars}"
                          " or less.")
            else:
                print("Your bet must be a positive integer.")
                pause()

    def player_wins_the_pot(self):
        self.player._dollars += (self._winnings * 2)
        self.player.display_dollars()

    def deal_cards(self):
        part1 = "The Dealer deals the Player"
        hand_size = TwentyOneGame._STARTING_HAND_SIZE
        part2 = "card"
        if hand_size > 1:
            part2 += "s"
        print(f"{part1} {hand_size} {part2}.")
        print(f"The Dealer draws {hand_size} {part2},"
              " both face-down.")
        print()
        for _ in range(hand_size):
            self.player.hit(self._deck)
            self.dealer.hit(self._deck)
        
        self.dealer.show_one_card()

    def reshuffle_deck(self):
        if len(self._deck._cards) < TwentyOneGame._DECK_THRESHOLD:
            print("The deck will be reset.")
            print("The discard pile is now empty.")
            self._deck.reset()
        else:
            print(f"The remaining {len(self._deck._cards)} cards"
                  " are shuffled.")
        print("...")
        pause()

    def player_turn(self):
        while True:
            self.player.show_hand()
            self.player.update_score()
            self.player.display_score()

            if (len(self.player._hand) == 
                TwentyOneGame._STARTING_HAND_SIZE):
                self.ante_up()

                self.player.show_hand()
                self.player.display_score()

            if self.player.is_busted():
                print("Darn! That's a bust!")
                print()
                break
            
            while True:
                print("What will you do?")
                print("-1: [H]it")
                print("-2: [S]tay")
                choice = input()

                if choice.lower() in ['1', 'h', '2', 's']:
                    break

                print("Invalid choice. Please choose '1' or '2'.")
                print()
            
            if choice.lower() in ['1', 'h']:
                print("You choose to take one more card.")
                print()
                self.player.hit(self._deck)

            if choice.lower() in ['2', 's']:
                print("You choose to stay.")
                print()
                break
            
    def dealer_turn(self):
        while True:
            if self.player.is_busted():
                break

            self.dealer.show_hand()
            self.dealer.update_score()
            self.dealer.display_score()

            if self.dealer.is_busted():
                print("Darn! That's a bust!")
                print()
                break
            if self.dealer.score >= 17:
                print("Dealer will stay.")
                print()
                break
            
            print("Dealer will hit.")
            self.dealer.hit(self._deck)

    def display_welcome_message(self):
        clear_screen()
        print("Welcome to Twenty One!")
        pause()
        print()

    def display_goodbye_message(self):
        print("Thanks for playing!")
        print()

    def display_result(self):
        self.player.display_score()
        self.dealer.display_score()

        if self.player.is_busted():
            print("Dealer wins!")
        elif self.dealer.is_busted():
            print("Player wins!")
            self.player_wins_the_pot()
        else:
            if self.player.score > self.dealer.score:
                print("Player wins!")
                self.player_wins_the_pot()
            elif self.player.score < self.dealer.score:
                print("Dealer wins!")
            else:
                print("Tie score! Dealer wins!")
        input()
    
    def play_again(self):
        while True:
            print("Would you like to play again?")
            print("-1: [Y]es")
            print("-2: [N]o")
            player_input = input()

            if player_input.lower() in ['1', 'y']:
                return True
            if player_input.lower() in ['2', 'n']:
                return False
            
            print("Invalid input. Please select '1' or '2'.")
            print()

game = TwentyOneGame()
game.start()