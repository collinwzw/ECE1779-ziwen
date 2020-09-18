"""
    Write a python function that implements a simple guessing game

    The function selects a secret value between 0 and 10 and
    returns the number of tries that it took the user to guess the secret

    In each try, if the guess is wrong, it lets the user know if the
    secret is larger or smaller than the last guess
"""
import random

def guessingGame(answer):
    '''
    (int) -> int
    Return how many tries it took for a user to guess a number
    '''
    guessCount = 1

    #ask user to provide a guess
    #check if the guess is euqal to value in answer
    #if yes, return the current value of guess count
    #otherwise, increment guess_count by one and try again

    guess = int(input("Please Guess the Number:"))

    while (guess != answer):
        guessCount += 1

        if guess > answer:
            hint = "Too large, guess again:"
        
        else:
            hint = "Too small, guess again:"

        guess = int(input(hint))

    return guessCount



tries = guessingGame(random.randint(0,10))
print("it tooks you", tries,"attempts")


#break#user1
#ece1779

