# # # class Car:
# # #     def __init__(self, model, year, color):
# # #         self._model = model
# # #         self._year = year
# # #         self.color = color
# # #         self._speed = 0
# # #         self._engine_on = False
    
# # #     @property
# # #     def color(self):
# # #         return self._color
    
# # #     @color.setter
# # #     def color(self, color):
# # #         if not isinstance(color, str):
# # #             print("Color must be a string.")
        
# # #         self._color = color
    
# # #     @property
# # #     def model(self):
# # #         return self._model
    
# # #     @property
# # #     def year(self):
# # #         return self._year

# # #     def engine_on(self):
# # #         if self._engine_on:
# # #             print("You hear a grinding noise. The engine was already on!")
# # #         else:
# # #             print("The engine roars to life!")
# # #             self._engine_on = True

# # #     def engine_off(self):
# # #         if self._engine_on:
# # #             print("The engine is now off.")
# # #             self._engine_on = False
            
# # #             if self._speed > 0:
# # #                 print("...")
# # #                 print("The car slowly rolls to a stop.")
# # #                 self._speed = 0

# # #         else:
# # #             print("The engine is already off.")

# # #     def accelerate(self, speed = 10):

# # #         if not self._engine_on:
# # #             print("Please turn on the engine first.")
# # #         else:
# # #             self._speed += speed
# # #             print("You step on the gas.")
# # #             self.current_speed()

# # #     def brake(self, speed = 10):
# # #         print("You step on the brakes.")

# # #         if not self._engine_on or self._speed == 0:
# # #             print("Nothing happens.")
        
# # #         else:
# # #             self._speed -= speed

# # #             if self._speed < 0:
# # #                 self._speed = 0
        
# # #         self.current_speed()

# # #     def current_speed(self):
# # #         print(f"The current speed is {self._speed}.")
    
# # #     @classmethod
# # #     def mpg(self, distance_mi, fuel_gal):
# # #         mpg = distance_mi / fuel_gal

# # #         print(f"This car has a fuel efficiency of {int(mpg)} miles per gallon.")

# # # car = Car("CRV", 2014, "gray")
# # # # car.brake()
# # # # print()
# # # # car.brake(10)
# # # # print()
# # # # car.engine_on()
# # # # print()
# # # # car.accelerate(20)
# # # # car.accelerate()
# # # # print()
# # # # car.engine_on()
# # # # car.current_speed()
# # # # print()
# # # # car.brake()
# # # # car.brake(30)
# # # # print()
# # # # car.current_speed()
# # # # car.engine_off()
# # # # print(car.year)
# # # # print(car.model)
# # # # print(car.color)
# # # # car.color = "red"
# # # # print(car.color)
# # # # car._model = "clarity"
# # # # print(car.model)
# # # Car.mpg(351, 13)

# # class Person:
# #     def __init__(self, first_name, last_name):
# #         self.first_name = first_name
# #         self.last_name = last_name
    
# #     @property
# #     def first_name(self):
# #         return self._first_name
    
# #     @first_name.setter
# #     def first_name(self, name):
# #         if not isinstance(name, str) or not name.isalpha():
# #             raise ValueError("Name must consist of alphabetic characters.")

# #         self._first_name = name
    
# #     @property
# #     def last_name(self):
# #         return self._last_name
    
# #     @last_name.setter
# #     def last_name(self, name):
# #         if not isinstance(name, str) or not name.isalpha():
# #             raise ValueError("Name must consist of alphabetic characters.")
        
# #         self._last_name = name
    
# #     def __str__(self):
# #         return f"{self.first_name.title()} {self.last_name.title()}"
    
# #     @property
# #     def name(self):
# #         return self.__str__()
    
# #     @name.setter
# #     def name(self, full_name):
# #         if not isinstance(full_name, tuple):
# #             raise ValueError("Full name must be a tuple.")
        
# #         self.first_name = full_name[0]
# #         self.last_name = full_name[1]


# # # actor = Person('Mark', 'Sinclair')
# # # print(actor.name)              # Mark Sinclair
# # # actor.name = ('Vin', 'Diesel')
# # # print(actor.name)              # Vin Diesel
# # # actor.name = ('', 'Diesel')
# # # # ValueError: Name must be alphabetic.

# # # character = Person('annIE', 'HAll')
# # # print(character.name)          # Annie Hall
# # # character = Person('Da5id', 'Meier')
# # # # ValueError: Name must be alphabetic.

# # friend = Person('Lynn', 'Blake')
# # print(friend.name)             # Lynn Blake
# # friend.name = ('Lynn', 'Blake-John')
# # # ValueError: Name must be alphabetic.

# class Car:
#     def __init__(self, model, year, color):
#         self._model = model
#         self._year = year
#         self._color = color
    
#     def __str__(self):
#         return f"{self._color.title()} {self._year} {self._model}"
    
#     def __repr__(self):
#         return f"Car({repr(self._model)}, {self._year}, {repr(self._color)})"

# vwbuzz = Car('ID.Buzz', 2024, 'red')
# print(vwbuzz)        # Red 2024 ID.Buzz
# print(repr(vwbuzz))  # Car('ID.Buzz', 2024, 'red')

import random

class GuessingGame:
    GUESSES = 7
    LOWEST = 1
    HIGHEST = 100

    def __init__(self):
        self._remaining_guesses = GuessingGame.GUESSES
        self._lowest_guess = GuessingGame.LOWEST
        self._highest_guess = GuessingGame.HIGHEST
        self.pick_new_secret_number(GuessingGame.LOWEST, GuessingGame.HIGHEST)
        self._player_guess = None

    def pick_new_secret_number(self, lowest, highest):
        self._secret_number = random.randint(lowest, highest)
    
    def print_guesses_remaining(self):
        print(f"You have {self._remaining_guesses} guesses remaining.")
    
    def ask_for_a_number(self):
        print(f"Enter a number between {GuessingGame.LOWEST} and"
              f"{GuessingGame.HIGHEST}:")
    
    def get_input_guess(self):
        while True:
            user_guess = input()

            if user_guess.isnumeric():
                if GuessingGame.LOWEST <= int(user_guess) <= GuessingGame.HIGHEST:
                    self._player_guess = user_guess
                    break
            
            print(f"Invalid guess. Guess must be a number between "
                  f"{GuessingGame.LOWEST} and {GuessingGame.HIGHEST}.")
    
    def check_guess(self, number):
        if self._player_guess < self._secret_number:
            print('Your guess is too low')
        elif self._player_guess > self._secret_number:
            print("Your guess is too high.")
        else:
            print("That's the number!")
    
    def show_result(self):
        if self._remaining_guesses == 0 or self._player_guess == self._secret_number:
            print("Game Over!")

    def play(self):
        self.print_guesses_remaining()
        self.ask_for_a_number()
        self.get_input_guess()