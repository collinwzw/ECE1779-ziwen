"""
    Write a python function that implements a simple guessing game

    The function selects a secret value between 0 and 10 and
    returns the number of tries that it took the user to guess the secret

    In each try, if the guess is wrong, it lets the user know if the
    secret is larger or smaller than the last guess
"""


import random

def guessing_game(answer):
    ''' (int) -> int
    Return how many tries it took for a user to guess a number.
    (no example, because we need input from the user)

    '''

    guess_count = 1     # tracks number of guesses

    # get initial guess from user
    # convert value to int
    guess = int(input("Guess the number:"))

    while guess != answer:
        guess_count += 1

        if guess > answer:
            hint = "Too large, guess again:"
        else:
            hint = "Too small, guess again:"

        guess = int(input(hint))


    return guess_count

tries = guessing_game(random.randint(0,9))

print("It took you",tries,"attempts.")
    