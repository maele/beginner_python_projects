import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: ')) #!!! parse input to int
        if guess < random_number:
            print('Sorry, guess again, too low.')
        elif guess > random_number:
            print('Sorry, guess again, too high!')
    print(f'Yay, congrats! You have guessed the number {random_number} correctly.')



def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c' and low != high:
        guess = random.randint(low, high)
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)?').lowercase()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print('Yay the computer guessed your number, {guess}, correctly!')



guess(10)