

# Rock-Paper-Scissor game

import emoji
import random
def play_game():

    print("Welcome to our childhood game")
choices = ['rock','paper','scissor']
while True:

    user = input("Choose your prop (rock,paper,scissor): ",).lower()
    if user == 'quit':
        print("Thanks for Playing")
        break
    elif user not in  choices:
        print("Invalid prop Enter right prop")
        continue
    computer = random.choice(choices)
    print(f"computer choose : {computer}")
    if user == computer:
        print("Its tie \U0001F61B")
    elif user == 'rock' and computer == 'paper' or user == 'scissor' and computer == 'paper'or user == 'rock' and computer == 'scissor':
        print("Congratulation you win \U0001F389 ")
    else:
        print("ohh you loose \U0001F622")
play_game()
