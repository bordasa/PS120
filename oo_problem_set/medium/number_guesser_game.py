import random
import os
import math

def clear_screen():
    return os.system('clear')

class GuessingGame:
    # _TOTAL_GUESSES = 7
    # _LOWEST_GUESS = 1
    # _HIGHEST_GUESS = 100

    def __init__(self, lowest_guess, highest_guess):
        self._LOWEST_GUESS = lowest_guess
        self._HIGHEST_GUESS = highest_guess
        self._TOTAL_GUESSES = (int(math.log2(self._HIGHEST_GUESS 
                                - self._LOWEST_GUESS + 1)) + 1)
        self.pick_new_number()
        self.player = Player(self._TOTAL_GUESSES)
        self.player_successful = False
    
    def play(self):
        self.welcome_message()

        while (self.player.guesses_left > 0 and 
               not self.player_successful):
            self.display_remaining_guesses()
            self.ask_for_guess()
            self.check_guess()
        
        self.display_result()

    def reset(self):
        self.__init__()

    def pick_new_number(self):
        self.answer = random.randint(self._LOWEST_GUESS,
                               self._HIGHEST_GUESS)

    def player_turn(self):
        pass
    
    def display_remaining_guesses(self):
        part1 = (f"You have {self.player.guesses_left}")
        guess_word = "guess"
        if self.player.guesses_left > 1:
            guess_word += 'es'

        print(f"{part1} {guess_word} remaining.")
    
    def enter_number_prompt(self):
        print(f"Enter a number between {self._LOWEST_GUESS}"
              f" and {self._HIGHEST_GUESS}:")

    def ask_for_guess(self):
        while True:
            self.enter_number_prompt()
            self.player.guess = input()

            if self.player.guess.isnumeric():
                self.player.guess = int(self.player.guess)

                if (self._LOWEST_GUESS <= self.player.guess
                    <= self._HIGHEST_GUESS):
                    self.player.guesses_left -= 1
                    break

                print("Invalid guess.")

            else:
                print("Invalid guess. Your guess must be an integer.")

    def check_guess(self):
        if self.player.guess < self.answer:
            print("Your guess is too low.\n")
        elif self.player.guess > self.answer:
            print("Your guess is too high.\n")
        else:
            print("That's the number!\n")
            self.player_successful = True

    def display_result(self):
        if self.player_successful:
            print("You won!")
        else:
            print("You have no more guesses. You lost!")
            print(f"The answer was: {self.answer}")

    def welcome_message(self):
        clear_screen()
        print("Let's play a guessing game!")
        print("I'm thinking of a number...")
        print()
    
class Player:
    def __init__(self, num_of_guesses):
        self.guesses_left = num_of_guesses
        self.guess = None

game = GuessingGame(1, 10)
game.play()
