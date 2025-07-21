# loop
running = True
while(running):
    # Choosing for operation modes
    mode = input("Mode: a / d / m / s / help / q (quit): ")
    inputted = str(mode)
    # Case-insensitive input
    inputted = inputted.lower()

    # Note that every mode is looking out for the ValueError, leading to failed operations and restarting the loop

    # Addition
    if(inputted=="a"):
        print("Addition Mode\n")
        try:
            number_one = float(input("First number: "))
            second_number = float(input("Second number: "))
        except ValueError:
            print("Please enter valid values.")
            continue
        calculated = (float(number_one) + float(second_number))
        print("Calculated:", str(calculated))

    # Division
    elif(inputted=="d"):
        print("Division Mode\n")
        try:
            number_one = float(input("First number: "))
            number_two = float(input("Second number: "))
        except ValueError:
            print("Please enter valid values.")
            continue

        # Throwing error when user want to divide by "0"
        if(number_two == 0):
            print("Error! Cannot divide by 0.. Try again!")
            continue
        else:
            calculated = (float(number_one) / float(number_two))
            print("Calculated: ", str(calculated))

    # Multiplication
    elif(inputted=="m"):
        print("Multiplication Mode\n")
        try:
            number_one = float(input("First number: "))
            number_two = float(input("Second number: "))
        except ValueError:
            print("Please enter valid values.")
            continue
        calculated = (float(number_one) * float(number_two))
        print("Calculated:", str(calculated))
    
    # Subtraction
    elif(inputted=="s"):
        print("Subtraction Mode\n")
        try:        
            number_one = float(input("First number: "))
            number_two = float(input("Second number: "))
        except ValueError:
            print("Please enter valid values.")
            continue
        calculated = (float(number_one) - float(number_two))
        print("Calculated:", str(calculated))
    
    # Overview of cocmmands using "help"
    elif(inputted=="help"):
        print("a: Addition \nd: Division\nm: Mulitplication\ns: Subtraction")

    # Quit
    elif(inputted=="q" or inputted=="quit"):
        # turning "running" to False, leading for the program to exit()
        print("Goodbye!")
        running = False
    
    # Any other input() is going to be detected as "Invalid"
    else:
        print("Invalid input, please try again\n")