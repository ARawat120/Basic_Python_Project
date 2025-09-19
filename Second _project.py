
# Number guessing game

import random
ran1 = random.randint(1,100)
while True:
    value = int(input("Guess the number between from 1 to 100: ",))
    if value >ran1:
        print("Your guess is too high!")
    elif value <ran1:
        print("Your guess is too low!")
    elif value == ran1:
        print("Congratulations! your guess is right")
        break
    else:
        print("Enter the number or valid range!!!")
