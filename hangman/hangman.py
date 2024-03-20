import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #what the user has guessed
    #getting user input
    lives = 6
    while len(word_letters) > 0 and lives > 0:
        #letters used:
        print(f'Letters used: ', ' '.join(used_letters))
        #what current word is like:
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(f'Current word: ',' '.join(word_list))
        user_letter = input('Guess a letter ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1
                print('Letter not in word')
        elif user_letter in used_letters:
            print('U already used that letter')
        else:
            print('Invalid character')
    if lives == 0:
        print('Sorry U died. The word was ', word)
    else:
        print('You guessed the word ;)', word)    

hangman()


