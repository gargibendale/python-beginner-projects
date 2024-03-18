import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('Guess again bro, too low')
        elif guess > random_number:
            print('Guess again, too high')
    print(f'You did it bro, you so real you guessed it, less go {random_number}')
        
guess(17)
