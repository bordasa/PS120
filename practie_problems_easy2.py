# class Game:
#     count = 0

#     def __init__(self, game_name):
#         Game.count += 1
#         self.game_name = game_name

#     def play(self):
#         return f'Start the {self.game_name} game!'

# class Bingo(Game):
#     def __init__(self, game_name, player_name):
#         self.player_name = player_name
#         super().__init__(game_name)

# class Scrabble(Game):
#     def __init__(self, game_name, player1_name, player2_name):
#         self.player_name1 = player1_name
#         self.player_name2 = player2_name
#         super().__init__(game_name)

# bingo = Bingo('Bingo', 'Bill')
# print(Game.count)                       # 1
# print(bingo.play())                     # Start the Bingo game!
# print(bingo.player_name)                # Bill

# scrabble = Scrabble('Scrabble', 'Jill', 'Sill')
# print(Game.count)                       # 2
# print(scrabble.play())                  # Start the Scrabble game!
# print(scrabble.player_name1)            # Jill
# print(scrabble.player_name2)            # Sill
# # print(scrabble.player_name)
# # AttributeError: 'Scrabble' object has no attribute 'player_name'

#Question3
#Benefits of OO Programming
#-More Modular (reuse prewritten code)
#- More easily maintainable (program is the interaction of many small parts instead of a big blob of dependencies)
#- Less repeated code
#- Better organization of code and logic (helps manage complexity)
# - classes and objects let programmers think about code at a more abstract level
# - allows programmers to create containers for data that can be changed and manipulated without affecting the entire program
# - We can talk about objects as nouns and methods as verbs, which makes it easier to conceptualize the structure of an OO program.
# - lets programmers write code that can be used with different kinds of data
