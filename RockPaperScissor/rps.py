import random, time

Hand = [
    "Rock",
    "Paper",
    "Scissor"
]
running = True

while running:
    userhand = input("Rock, Paper Scissor? (r,p,s): ").strip().lower()
    if(userhand == "r"):
        userhand = "Rock"
    elif(userhand =="p"):
        userhand = "Paper"
    elif(userhand == "s"):
        userhand = "Scissor"
    else:
        print("Please enter a valid option.")
    
    aihand = random.choice(Hand)
    print("Rock!")
    time.sleep(0.5)
    print("Paper!")
    time.sleep(0.5)
    print("Scissor!")
    time.sleep(0.5)
    if userhand == aihand:
        print(f"Draw! You: {userhand}  PC: {aihand}")
    elif (userhand == "Rock" and aihand == "Scissor") or \
        (userhand == "Paper" and aihand == "Rock") or \
        (userhand == "Scissor" and aihand == "Paper"):
            print(f"You won! You: {userhand}  PC: {aihand}")
    else:
        print(f"You lost! You: {userhand}  PC: {aihand}")
    choice = input("\nTry again? (y/n)").strip().lower()
    if (choice == "y"):
        continue
    elif (choice == "n"):
        running = False
    else:
        print("No valid choice. Exiting..")
        running = False
    