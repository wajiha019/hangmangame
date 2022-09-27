import random
from typing import List

# TODO try to load these from a text file
WORD_LIST = open('words.txt','r')
WORD_LIST=WORD_LIST.readline()
WORD_LIST=str.split(WORD_LIST)
GUESS_WORD = []
SECRET_WORD = random.choice(WORD_LIST) # lets randomize single word from the list
LENGTH_WORD = len(SECRET_WORD)
ALPHABET='abcdefghijklmnopqrstuvwxyz'
alpha=list(ALPHABET)
letter_storage = []

# Utility functions

def print_word_to_guess(letters: List):
    """Utility function to print the current word to guess"""
    print("Word to guess: {0}".format(" ".join(letters)))


def print_guesses_taken(current, total):
    """Prints how many chances the player has used"""
    print(f"You are on guess {current}/{total}")
def print_warnings(current, total):
    """Prints how many chances the player has used"""
    print(f"You are on warning {current}/{total}")

def remove_guess(guess):
        alpha.remove(guess)
        a=len(alpha)
        print('Available letters:',end='')
        for i in alpha:
            if a==1:
                print(i)
            else:
                print(i,end='')
            a-=1

            
# Game functions


def prepare_secret_word():
    """Prepare secret word and inform user of it"""
    for character in SECRET_WORD: # printing blanks for each letter in secret word
        GUESS_WORD.append("-")
    print("Loading word list from file....\n55900 words loaded.\nWelcome to the game Hangman!\nI am thinking of a word that is", LENGTH_WORD, "letters long")
    print("Be aware that You can enter only 1 letter from a-z\n\n")
    print_word_to_guess(GUESS_WORD)


def guessing():
    """
    Main game loop to have user guess letters
    and inform them of the results
    """
    guess_taken = 0
    MAX_GUESS = 6
    MAX_WARNINGS=3
    warnings_left=0
    hanger=['''
                 _____
                |     |
                      |
                      |
                      |
                      |_''', '''
                 _____
                |     |
                O   |
                      |
                      |
                      |_''', '''
                 _____
                |     |
                O   |
                |     |
                |     |
                      |_''', '''
                 _____
                |     |
                O   |
               /|     |
                |     |
                      |_''', '''
                 _____
                |     |
                O   |
               /|\    |
                |     |
                      |_''', ''' 
                 _____
                |     |
                O   |
               /|\    |
                |     |
               /      |_''', '''
                 _____
                |     |
                O   |
               /|\    |
                |     |
               / \    |_''','''
       ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆
       ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆    
                
                   \O/    
~WINNER~   ||   ~WINNER~        
                     |   
                    / \ 
                                       
       ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆
       ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆''']
    print_guesses_taken(guess_taken, MAX_GUESS)

    while guess_taken < MAX_GUESS:
        if letter_storage==[]:
            print('Available letters:',ALPHABET)
            guess = input("Pick a letter : ").lower()
            
        else:
            remove_guess(guess)
            guess = input("Pick a letter : ").lower()
        if guess not in ALPHABET and warnings_left!=3:#checking input
            print("Enter a letter from a-z ALPHABET")
            warnings_left+=1
            print_warnings(warnings_left,MAX_WARNINGS)
            print_guesses_taken(guess_taken, MAX_GUESS)
        elif warnings_left==3 and guess not in ALPHABET:
            print("Enter a letter from a-z ALPHABET")
            guess_taken+=1
            print('you have no warnings left so you lost one guess')
            print_guesses_taken(guess_taken, MAX_GUESS)
            if guess_taken!=7:
                    print(hanger[guess_taken])
            if guess_taken == 6:
                    print(f"Sorry Mate, You lost :<! The secret word was : {SECRET_WORD}")
                    break
        elif guess in letter_storage and warnings_left!=3 : #checking if letter has been already used
            print("You have already guessed that letter!")
            warnings_left+=1
            print_warnings(warnings_left,MAX_WARNINGS)
            print_guesses_taken(guess_taken, MAX_GUESS)
        elif warnings_left==3 and guess in letter_storage :
            guess_taken+=1
            print("You have already guessed that letter!")
            print('you have no warnings left so you lost one guess')
            print_guesses_taken(guess_taken, MAX_GUESS)
            if guess_taken!=7:
                    print(hanger[guess_taken])
            if guess_taken == 6:
                    print(f"Sorry Mate, You lost :<! The secret word was : {SECRET_WORD}")
                    break
        elif guess in 'aeiou' and guess not in SECRET_WORD:
            letter_storage.append(guess)
            guess_taken+=2
            print('you guess a letter which is not in SECRET_WORD so you loss 2 guesses')
            if guess_taken!=7:
                    print(hanger[guess_taken])
            if guess_taken >= 6:
                    print(f"Sorry Mate, You lost :<! The secret word was : {SECRET_WORD}")
                    break
            print_guesses_taken(guess_taken, MAX_GUESS)
        else: 
            letter_storage.append(guess)
            if guess in SECRET_WORD:
                print("You guessed correctly!")
                for i in range(0, LENGTH_WORD):
                    if SECRET_WORD[i] == guess:
                        GUESS_WORD[i] = guess
                print_word_to_guess(GUESS_WORD)
                print_guesses_taken(guess_taken, MAX_GUESS)
                if '-' not in GUESS_WORD:
                    print(hanger[7])
                    print("You won!")
                    print("Game Over!")
                    break
            else:
                print("The letter is not in the word. Try Again!")
                guess_taken += 1
                print(hanger[guess_taken])
                print_guesses_taken(guess_taken, MAX_GUESS)
                if guess_taken == 6:
                    print(f"Sorry Mate, You lost :<! The secret word was : {SECRET_WORD}")

prepare_secret_word()
guessing()
