import random
import string
from words import words

def get_valid_word(words):
    word = random.choice(words) #randomly picks word from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper() #fixed! Wtihout upper() Current word won't update with input letters

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) #letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #what the user has guessed

    lives = 6

    #user input
    while len(word_letters) > 0 and lives > 0:
        #letters used
        #' '.join*['a', 'b', 'cd']) --> 'a b cd'
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))

        #what current word is
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives = lives - 1 #takes away a life if wrong
                print('Letter is not in word.')

        elif user_letter in used_letters:
            print('You have already used that character. Try again.')

        else:
            print('Invalid character. Please try again.')
    #gets here when len(word_letters) == 0 or when lives == 0
    if lives == 0:
        print('You died, sorry. The word was', word)
    else:
        print('You guessed the word', word, '!!')

hangman()