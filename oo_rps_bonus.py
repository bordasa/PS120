import random

class Move:
    def __init__(self):
        self._name = None
        self._wins_against = None
    
    @property
    def name(self):
        return self._name

    def wins(self, other_move):
        return other_move.name.lower() in self._wins_against

class Rock(Move):
    def __init__(self):
        super().__init__()
        self._name = 'rock'
        self._wins_against = ['scissors', 'lizard']

class Paper(Move):
    def __init__(self):
        super().__init__()
        self._name = 'paper'
        self._wins_against = ['rock', 'spock']

class Scissors(Move):
    def __init__(self):
        super().__init__()
        self._name = 'scissors'
        self._wins_against = ['paper', 'lizard']

class Lizard(Move):
    def __init__(self):
        super().__init__()
        self._name = 'lizard'
        self._wins_against = ['spock', 'paper']

class Spock(Move):
    def __init__(self):
        super().__init__()
        self._name = 'spock'
        self._wins_against = ['scissors', 'rock']

class Player:
    CHOICES = [move() for move in Move.__subclasses__()]

    def __init__(self):
        self.move = None
        self.score = 0
        self._move_history = []

class Human(Player):
    def __init__(self):
        super().__init__()

    def choose(self):
        while True:
            print('Please choose your move:')
            for index, choice in enumerate(Player.CHOICES, 1):
                print(f"- {index}. {choice.name.title()}")

            player_choice = input()

            if player_choice in [str(num) for num in range(1, len(Player.CHOICES) + 1)]:
                break

            print(f'Invalid input. Please input a number 1 - {len(Player.CHOICES)}.')

        self.move = Player.CHOICES[int(player_choice) - 1]
        self._move_history.append(self.move)

class Computer(Player):
    def __init__(self):
        super().__init__()
        self.name = random.choice(['Computer', 'R2D2', 'HAL', 'Daneel'])

    def choose(self, human):
        match self.name:
            case 'Computer':
                self.move = random.choice(Player.CHOICES)
            case 'R2D2':
                self.move = Rock()
            case 'HAL':
                self.move = random.choice(Player.CHOICES + [Scissors()] * 3)
            case 'Daneel':
                if len(human._move_history) > 1:
                    self.move = human._move_history[-2]
                else:
                    self.move = random.choice(Player.CHOICES)
        
        self._move_history.append(self.move)

class RPSGame:
    def __init__(self):
        self._human = Human()
        self._computer = Computer()

    def _display_welcome_message(self):
        print('Welcome to Rock Paper Scissors Lizard Spock!')
        print('The game ends when someone wins 5 points!')
        print(f'Your opponent this game will be {self._computer.name}.\n')

    def _display_goodbye_message(self):
        print('Thanks for playing!\n')

    def _display_winner(self):
        print(f'You chose: {self._human.move.name}')
        print(f'{self._computer.name} chose: {self._computer.move.name}')

        if self._human.move.wins(self._computer.move):
            print('You win!\n')
            self._human.score += 1

        elif self._computer.move.wins(self._human.move):
            print(f'{self._computer.name} wins!\n')
            self._computer.score += 1

        else:
            print("It's a tie!\n")

        print(f'Your score: {self._human.score} / Last move: {self._human._move_history[-1].name}')
        print(f"{self._computer.name}'s score: {self._computer.score} / Last move: {self._computer._move_history[-1].name}")
        print()

    def _play_again(self):
        while True:
            print('Would you like to play again? (y/n)')
            play_again_input = input()

            if play_again_input.lower()[0] in ['y', 'n']:
                break

            print("Invalid input. Please type 'yes' or 'no'.")

        return play_again_input.lower().startswith('y')

    def play(self):
        self._display_welcome_message()

        while True:
            while True:
                self._human.choose()
                self._computer.choose(self._human)
                self._display_winner()

                if self._human.score == 5:
                    print("Game over. You won 5 games!\n")
                    self._human.score = 0
                    self._computer.score = 0
                    break
                
                if self._computer.score == 5:
                    print(f"Game over. {self._computer.name} won 5 games!\n")
                    self._human.score = 0
                    self._computer.score = 0
                    break

            if not self._play_again():
                break

        self._display_goodbye_message()

RPSGame().play()
