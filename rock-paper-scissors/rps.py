import random

def play():
    user = input("'r' for rock, 'p' for paper, 's' for scissors: ")
    computer = random.choice(['r', 'p', 's'])
    if user == computer:
        print('It\'s a tie!')
    elif is_win(user, computer):
        print(computer)
        print('You won!')
    print(computer)
    print('You lost :(')
def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
play()
