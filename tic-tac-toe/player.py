import math
import random

class Player:
    def __init__(self, letter):
        #letter is x or o
        self.letter =  letter

    #we want all the players to be able to get their next move
    def get_move(self, game):
        pass

class RandomComputer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-9)')
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square, enter again')
        return val