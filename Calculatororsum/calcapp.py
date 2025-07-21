import tkinter as tk
import time
current_number = "0"
number1 = None
second = False
which = ""

def add_digit(digit):
    global current_number, second, number1

    if not second:
        if current_number == "0":
            current_number = digit
        else:
            current_number += digit
    else:
        # start second number entry
        current_number = digit
        second = False  # reset for next input

    label.config(text=current_number)

def addition():
    global current_number, number1, second, which
    which = "addition"
    number1 = int(current_number)
    second = True
    label.config(text=f"{number1} + ")

def equals():
    global current_number, number1
    number2 = int(current_number)
    if(which=="addition"):
        result = number1 + number2
        label.config(text=f"{number1} + {number2} = {result}")
    # Reset everything for new calculation
        current_number = str(result)
    if(which=="divide"):
        if(number2 == 0):
            label.config("try again!")
            time.sleep(1)
            current_number = "0"
            number1, number2 = 0
            label.config(text=f"{current_number}")
        else:    
            result = number1 / number2
            label.config(text=f"{number1} / {number2} = {result}")

    
def reset():
    global current_number, number1
    current_number = "0"
    number1 = 0
    label.config(text=f"{current_number}")
    
def divide():
    global current_number, number1, second, which
    number1 = int(current_number)
    second = True
    label.config(text=f"{number1} / ")
    which = "divide"

root = tk.Tk()
root.title("Simple Calculator")
root.geometry("400x300")

label = tk.Label(root, text=str(current_number), font=("Arial", 20))
label.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack()

# Digit buttons
for i in range(1, 10):
    btn = tk.Button(button_frame, text=str(i), width=5, height=2,
                    command=lambda d=str(i): add_digit(d))
    btn.grid(row=(i-1)//3, column=(i-1)%3)

btn0 = tk.Button(button_frame, text="0", width=5, height=2,
                 command=lambda: add_digit("0"))
btn0.grid(row=3, column=1)

# + button
btnadd = tk.Button(button_frame, text="+", width=5, height=2,
                   command=addition)
btnadd.grid(row=0, column=3)

# = button
btnequal = tk.Button(button_frame, text="=", width=5, height=2,
                     command=equals)
btnequal.grid(row=2, column=3)

btndivide = tk.Button(button_frame, text="/", width=5, height=2,
                      command=divide)
btndivide.grid(row=1, column=3)
btnreset = tk.Button(button_frame, text="reset", width=5, height=2,
                     command = reset)
btnreset.grid(row=3, column=3)

root.mainloop()