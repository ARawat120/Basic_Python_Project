# Hangman Game
print("Enter a country name")
word = input().lower()
life_line = 6
print(f"guess the letter in {life_line} lifeline")
while life_line>0:
    key = input().lower()
    if key in word:
        print(word,"contain",key)
        word = word.replace(key,"")
        print(len(word))
        if len(word)==0:
            print("you win!!!!!!! ")
            break

    else:
        life_line -=1
        print("your guess is wrong!!")
        if life_line == 0:
            print("your loose (lifeline was finished) !!")
            break

