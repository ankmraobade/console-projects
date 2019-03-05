# Rock Paper Scissors

"""
Make a two-player Rock-Paper-Scissors game.
Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game.
Rules:
1. Rock beats scissors
2. Scissors beats paper
3. Paper beats rock
"""

from random import *
from sys import *

computerPoints = 0
humanPoints = 0

# MAIN MENU

print("-------------------")
print("ROCK PAPER SCISSORS")
print("-------------------")
print("-------MENU--------")
print("`\t1. New Game")
print("`\t2. Help")
print("`\t3. Quit")

gameSelect = int(input("Enter Your Choice [1, 2, 3] from above: "))

while gameSelect != 3:

    if gameSelect == 1:
        print("-------------------")
        print("ROCK PAPER SCISSORS")
        print("-------------------")
        print("1. Rock 2. Paper 3. Scissors")

        choiceList = {1: "rock", 2: "paper", 3: "scissors"}

        computerChoice = choice(list(choiceList))

        humanChoice = int(input("Enter Your Choice [1, 2, 3]: "))

        if humanChoice == 1:
            print("You chose Rock")

            if computerChoice == 1:
                print("Computer chose Rock")
                print("Match Drawn")
                print("Computer Points: ", computerPoints)
                print("Human Points: ", humanPoints)
            elif computerChoice == 2:
                print("Computer chose Paper")
                print("Computer Wins")
                computerPoints += 1
                print("Computer Points: ", computerPoints)
                print("Human Points: ", humanPoints)
            else:
                print("Computer chose Scissors")
                print("Congratulations! You Win")
                humanPoints += 1
                print("Computer Points: ", computerPoints)
                print("Human Points: ", humanPoints)
        elif humanChoice == 2:
            print("You chose Paper")

            if computerChoice == 1:
                print("Computer chose Rock")
                print("Congratulations! You Win")
                humanPoints += 1
                print("Computer Points: ", computerPoints)
                print("Human Points: ", humanPoints)
            elif computerChoice == 2:
                print("Computer chose Paper")
                print("Match Drawn")
                print("Computer Points: ", computerPoints)
                print("Human Points: ", humanPoints)
            else:
                print("Computer chose Scissors")
                print("Computer Wins")
                computerPoints += 1
                print("Computer Points: ", computerPoints)
                print("Human Points: ", humanPoints)
        elif humanChoice == 3:
            print("You chose Scissors")

            if computerChoice == 1:
                print("Computer chose Rock")
                print("Computer Wins")
                computerPoints += 1
                print("Computer Points: ", computerPoints)
                print("Human Points: ", humanPoints)
            elif computerChoice == 2:
                print("Computer chose Paper")
                print("Congratulations! You Win")
                humanPoints += 1
                print("Computer Points: ", computerPoints)
                print("Human Points: ", humanPoints)
            else:
                print("Computer chose Scissors")
                print("Match Drawn")
                print("Computer Points: ", computerPoints)
                print("Human Points: ", humanPoints)

        user_choice_to_play = input("Do you want to play again? (Y/N): ")

        if user_choice_to_play == 'Y' or user_choice_to_play == 'y':
            continue
        elif user_choice_to_play == 'N' or user_choice_to_play == 'n':
            break
        else:
            print("Invalid choice. Please try again.")

        continue
    elif gameSelect == 2:
        print("Rock beats Scissors. Scissors beats Paper. Paper beats Rock")
        exit()
    else:
        print("Invalid Choice. Please try again.")
        exit()

print("Thank you for using ROCK PAPER SCISSORS!")
exit()
            
