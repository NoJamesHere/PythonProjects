import random

number = random.randint(1, 100)
running = True
trys = 0
print("Guess the number! Ranging from 1 to 100!")
while running:
    command = input()
    if(int(command) == number):
        print(f"CORRECT! The number you guessed was {number}, CONGRATS!\nYour number of guesses:{trys}")
        running = False
    elif(int(command) > number):
        print("Lower")
        trys += 1
    elif(int(command) < number):
        print("Higher")
        trys += 1