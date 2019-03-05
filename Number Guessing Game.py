# Number Guessing Game

"""
Generate a random number between 1 and 9 (including 1 and 9).
Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.

Extras:
1. Keep the game going until the user types "exit"
2. Keep track of how many guesses the user has taken and when the game ends, print this out.
"""

from random import *
from sys import *

guess_count = 0

print("--------------------")
print("NUMBER GUESSING GAME")
print("--------------------")

user_command = input("Enter Your Choice: [ANY Key to Play OR type 'exit' to Quit]: ")

while user_command != "exit":

    number = randint(1, 9)
    
    user_guess = int(input("Enter Your Guess from 1 to 9:" ))

    guess_count += 1

    if user_guess >= 1 and user_guess <= 9:
        if number == user_guess:
            print("Congratulations! Your guess is absolutely correct.")
        else:
            print("Sorry, Wrong Guess!")

            if number < user_guess:
                print("You guessed too high")
                print("The actual number is: ", number)
            else:
                print("You guessed too low")
                print("The actual number is: ", number)
    else:
        print("Invalid Input. Please enter between 1 to 9.")

    user_choice_to_play = input("Do you want to play again? (Y/N): ")

    if user_choice_to_play == 'Y' or user_choice_to_play == 'y':
        continue
    elif user_choice_to_play == 'N' or user_choice_to_play == 'n':
        break
    else:
        print("Invalid choice. Please try again.")

    continue

print("Thank you for playing the GUESSING GAME")
print("Total number of guesses by user: ", guess_count)
exit()
