import random
import os

def clear_screen():
    os.system('clear')

class Square:
    INITIAL_MARKER = " "
    HUMAN_MARKER = "X"
    COMPUTER_MARKER = "O"

    def __init__(self, marker=INITIAL_MARKER):
        self.marker = marker

    def __str__(self):
        return self.marker

    @property
    def marker(self):
        return self._marker

    @marker.setter
    def marker(self, marker):
        self._marker = marker

    def is_unused(self):
        return self.marker == Square.INITIAL_MARKER

class Board:
    def __init__(self):
        self.reset()

    def reset(self):
        self.squares = {key: Square() for key in range(1, 10)}

    def display(self):
        print()
        print("     |     |")
        print(f"  {self.squares[1]}  |"
              f"  {self.squares[2]}  |"
              f"  {self.squares[3]}")
        print("     |     |")
        print("-----------------")
        print("     |     |")
        print(f"  {self.squares[4]}  |"
              f"  {self.squares[5]}  |"
              f"  {self.squares[6]}")
        print("     |     |")
        print("-----------------")
        print("     |     |")
        print(f"  {self.squares[7]}  |"
              f"  {self.squares[8]}  |"
              f"  {self.squares[9]}")
        print("     |     |")

    def display_with_clear(self):
        clear_screen()
        print("\n")
        self.display()

    def mark_square_at(self, key, marker):
        self.squares[key].marker = marker

    def unused_squares(self):
        return [key
                for key, square in self.squares.items()
                if square.is_unused()]

    def is_full(self):
        return len(self.unused_squares()) == 0

    def count_markers_for(self, player, keys):
        markers = [self.squares[key].marker for key in keys]
        return markers.count(player.marker)
    
    def find_unused_square_for(self, keys):
        for key in keys:
            if self.squares[key].marker == Square.INITIAL_MARKER:
                return key
        return None

class Player:
    def __init__(self, marker):
        self.marker = marker
        self.score = 0

    @property
    def marker(self):
        return self._marker

    @marker.setter
    def marker(self, value):
        self._marker = value

    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, value):
        self._score = value
    
    def increment_score(self):
        self.score += 1

class Human(Player):
    def __init__(self):
        super().__init__(Square.HUMAN_MARKER)

class Computer(Player):
    def __init__(self):
        super().__init__(Square.COMPUTER_MARKER)

class TTTGame:
    MATCH_GOAL = 3

    POSSIBLE_WINNING_ROWS = (
        (1, 2, 3),
        (4, 5, 6),
        (7, 8, 9),
        (1, 4, 7),
        (2, 5, 8),
        (3, 6, 9),
        (1, 5, 9),
        (3, 5, 7),
    )

    def __init__(self):
        self.board = Board()
        self.human = Human()
        self.computer = Computer()
        self._tie_games = 0

    @staticmethod
    def _join_or(my_list, separator=', ', conjunction='or'):
        my_str_list = [str(num) for num in my_list]

        if len(my_list) == 1:
            return my_str_list[0]
        if len(my_list) == 2:
            return f"{my_str_list[0]} {conjunction} {my_str_list[1]}"
        
        part1 = separator.join(my_str_list[: -1])
        part2 = f"{conjunction} {my_str_list[-1]}"
        return f"{part1}{separator}{part2}"

    def display_scores(self):
        print(f"Your Score: {self.human.score}")
        print(f"Computer Score: {self.computer.score}")
        print(f"Ties: {self._tie_games}")

    def display_ui(self):
        clear_screen()
        print("---Tic Tac Toe ---")
        self.board.display()
        self.display_scores()
        print()

    def human_moves(self):
        while True:
            valid_choices = self.board.unused_squares()
            choices_list = [str(choice) for choice in valid_choices]
            choices_str = TTTGame._join_or(choices_list)
            prompt = f"Choose a square ({choices_str}): "
            choice = input(prompt)

            try:
                choice = int(choice)
                if choice in valid_choices:
                    break
            except ValueError:
                pass

            print("Sorry, that's not a valid choice.")
            print()

        self.board.mark_square_at(choice, self.human.marker)

    def computer_moves(self):
        choice = self.winning_move()

        if not choice:
            choice = self.blocking_move()
        if not choice:
            choice = self.pick_center_square()
        if not choice:
            choice = self.pick_random_square()
        
        self.board.mark_square_at(choice, self.computer.marker)

    def player_moves(self, current_player):
        if current_player == self.human:
            return self.human_moves()
        else:
            return self.computer_moves()

    def toggle_player(self, current_player):
        if current_player == self.human:
            return self.computer
        else:
            return self.human

    def display_welcome_message(self):
        clear_screen()
        print('Welcome to Tic Tac Toe!')
        print("Press <Enter> to begin!")
        input()

    def display_goodbye_message(self):
        if self.human.score > self.computer.score:
            print('You are the champion!')
        elif self.computer.score > self.human.score:
            print('I am the champion!')
        else:
            print('We are both champions!')
        
        print()
        self.display_scores()
        print()
        print('Thanks for playing Tic Tac Toe! Goodbye!')

    def display_results(self):
        if self.is_winner(self.human):
            self.human.score += 1
            print("You won! Congratulations!")
        elif self.is_winner(self.computer):
            self.computer.score += 1
            print("I won! I won! Take that, human!")
        else:
            self._tie_games += 1
            print("A tie game. How boring.")
        
        print()

    def play_again(self):
        while True:
            keep_playing = input("Would you like to play again? (y/n)\n")

            if keep_playing.lower() in ('y', 'n'):
                return keep_playing.lower() == 'y'

            print("Invalid input. Please input 'y' or 'n'.\n")

    def is_game_over(self):
        return self.board.is_full() or self.someone_won()

    def three_in_a_row(self, player, row):
        return self.board.count_markers_for(player, row) == 3
    
    def two_in_a_row(self, player, row):
        return self.board.count_markers_for(player, row) == 2

    def someone_won(self):
        return (self.is_winner(self.human) or
                self.is_winner(self.computer))

    def is_winner(self, player):
        for row in TTTGame.POSSIBLE_WINNING_ROWS:
            if self.three_in_a_row(player, row):
                return True

        return False
    
    def winning_or_blocking_move(self, player):
        options = []
        for row in TTTGame.POSSIBLE_WINNING_ROWS:
            if self.two_in_a_row(player, row):
                options.append(self.board.find_unused_square_for(row))
        
        valid_options = [move for move in options
                         if move in self.board.unused_squares()]
        
        try:
            return valid_options[0]
        except IndexError:
            return None
    
    def winning_move(self):
        return self.winning_or_blocking_move(self.computer)
    
    def blocking_move(self):
        return self.winning_or_blocking_move(self.human)
    
    def pick_center_square(self):
        if 5 in self.board.unused_squares():
            return 5
        return None
    
    def pick_random_square(self):
        valid_choices = self.board.unused_squares()
        return random.choice(valid_choices)

    def who_goes_first(self):
        while True:
            print("Who should go first?")
            print("- 1: Me! The human!")
            print("- 2: You! The computer!")
            player_input = input()

            if player_input == "1":
                return self.human
            if player_input == "2":
                return self.computer
            
            print("Invalid choice. Please select '1' or '2'.")

    def play(self):
        self.display_welcome_message()
        first_player = self.who_goes_first()

        while True:

            self.play_one_game(first_player)

            if (self.human.score == self.MATCH_GOAL or
               self.computer.score == self.MATCH_GOAL):
                print("That's 3 wins!")
                input()
                break
            
            if not self.play_again():
                print("Quitting early? I guess that means...")
                input()
                break
            
            print("Let's play again!")
            print()
            first_player = self.toggle_player(first_player)

        clear_screen()
        self.display_goodbye_message()

    def play_one_game(self, first_player):
        self.board.reset()
        self.display_ui()

        current_player = first_player

        while True:
            self.player_moves(current_player)
            if self.is_game_over():
                break
        
            self.display_ui()
            current_player = self.toggle_player(current_player)
        
        self.display_ui()
        self.display_results()

game = TTTGame()
game.play()
