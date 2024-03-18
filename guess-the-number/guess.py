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
    print(f"You did it bro, you so real you guessed it, less go {random_number}")

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c' :
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f'Is {guess} too high (H), too low(L) or correct (C)?').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f'Yay, the computer guessed the no. {guess} correctly!')
        
computer_guess(13)
