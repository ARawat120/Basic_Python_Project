
# Rolling dice game

import random
count = 0
while True:
    choice = input("Rolling the dice(y/n): ",).lower()
    if choice == 'y':
        ran1 = random.randint(1,6)
        ran2 = random.randint(1, 6)
        print(f"{(ran1,ran2)}")
        count+=1
    elif choice =='n':
        print("Thanks for playing!")
        print(f"{count} times the dice rolling")
        break
    else:
        print("Invalid input!!!!")