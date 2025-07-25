import random
import time

running = True
while running:
    dice_faces = {
    1: "⚀",
    2: "⚁",
    3: "⚂",
    4: "⚃",
    5: "⚄",
    6: "⚅"
    }
    for i in range(9):
        number = random.randint(1,6)
        print (f"Dice: {number}")
        time.sleep(0.5)

    time.sleep(1.5)
    number = random.randint(1,6)
    if(number == 1):
        print(f"Diced! {dice_faces[number]}")
        print("Oof, you rolled a 1. Better luck next time!")
    elif(number == 6):
        print(f"Diced! {dice_faces[number]}")
        print("WOW! You rolled a 6! That's the best you can get!")
    else:
        print(f"Diced! {dice_faces[number]}")
        print(f"You rolled a {number}. Not bad, but could be better!")
    choice = input("Do you wanna try again? (y/n): ").lower()
    if(choice == "y"):
        continue
    elif(choice=="n"):
        print("Goodbye")
        running = False
    else:
        print("Invalid input. Closing program..")
        running = False