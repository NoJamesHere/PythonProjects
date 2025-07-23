import random

number = random.randint(1, 100)
running = True
trys = 0
print("Guess the number! Ranging from 1 to 100!")
while running:
    command = input()

    if not command.isdigit():
        print("Please enter an actual number..")
        continue
    guess = int(command)
    if (guess < 1 or guess > 100):
        print("The number to guess ranges from 100 to 1, try again..")
        continue
    if(guess == number):
        if(trys == 0):
            print(f"WOW! YOU GUESSED THE NUMBER {number} ON FIRST TRY!")
        else:
            print(f"CORRECT! The number you guessed was {number}, CONGRATS!\nYour number of guesses:{trys}")
            running = False
    elif(guess > number):
        print("Lower")
        trys += 1
    elif(guess < number):
        print("Higher")
        trys += 1