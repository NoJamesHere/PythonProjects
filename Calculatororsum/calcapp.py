import tkinter as tk

current_number = "0"
number1 = None
second = False
which = ""
result_displayed = False

def add_digit(digit):
    global current_number, second, number1, result_displayed

    if result_displayed:
        current_number = digit
        result_displayed = False
    elif not second:
        if current_number == "0":
            current_number = digit
        else:
            current_number += digit
    else:
        # start second number entry
        current_number = digit
        second = False

    label.config(text=current_number)

def addition():
    global current_number, number1, second, which
    which = "addition"
    number1 = int(current_number)
    second = True
    label.config(text=f"{number1} + ")

def divide():
    global current_number, number1, second, which
    which = "divide"
    number1 = int(current_number)
    second = True
    label.config(text=f"{number1} / ")

def subtract():
    global current_number, number1, second, which
    which = "subtract"
    number1 = int(current_number)
    second = True
    label.config(text=f"{number1} - ")

def multiply():
    global current_number, number1, second, which
    which = "multiply"
    number1 = int(current_number)
    second = True
    label.config(text=f"{number1} * ")

def equals():
    global current_number, number1, result_displayed
    try:
        number2 = int(current_number)
    except ValueError:
        label.config(text="Invalid input")
        return

    if which == "addition":
        result = number1 + number2
        label.config(text=f"{number1} + {number2} = {result}")
    elif which == "subtract":
        result = number1 - number2
        label.config(text=f"{number1} - {number2} = {result}")
    elif which == "multiply":
        result = number1 * number2
        label.config(text=f"{number1} * {number2} = {result}")
    elif which == "divide":
        if number2 == 0:
            label.config(text="try again!")
            root.after(2000, lambda: label.config(text=current_number))
            current_number = "0"
            number1 = 0
            return
        else:
            result = number1 / number2
            label.config(text=f"{number1} / {number2} = {result}")

    current_number = str(result)
    number1 = 0
    result_displayed = True

def reset():
    global current_number, number1, second, which, result_displayed
    current_number = "0"
    number1 = 0
    second = False
    which = ""
    result_displayed = False
    label.config(text=current_number)

# --- GUI setup ---
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("380x380")
root.configure(bg="#ffd4ba")
label = tk.Label(root, text=str(current_number), font=("Helvetica", 28, "bold"),
                 bg="#1d0505", fg="white", anchor="e", padx=10)
label.pack(pady=20, fill="x")

button_frame = tk.Frame(root)
button_frame.pack()

button_style = {
    "width": 5,
    "height": 2,
    "font": ("Helvetica", 14),
    "bg": "#2e2e2e",
    "fg": "white",
    "activebackground": "#444",
    "activeforeground": "white",
    "bd": 0,
    "highlightthickness": 0,
    "relief": "flat"
}

button_style2 = {
    "width": 5,
    "height": 2,
    "font": ("Helvetica", 14),
    "bg": "#310e0e",
    "fg": "white",
    "activebackground": "#444",
    "activeforeground": "white",
    "bd": 0,
    "highlightthickness": 0,
    "relief": "flat"
}

for i in range(1, 10):
    btn = tk.Button(button_frame, text=str(i), **button_style,
                    command=lambda d=str(i): add_digit(d))
    btn.grid(row=(i-1)//3, column=(i-1)%3, padx=5, pady=5)

btn0 = tk.Button(button_frame, text="0", **button_style,
                 command=lambda: add_digit("0"))
btn0.grid(row=3, column=1, padx=5, pady=5)


# Operator buttons
btnadd = tk.Button(button_frame, text="+", **button_style2, command=addition)
btnadd.grid(row=0, column=3, padx=5, pady=5)

btndivide = tk.Button(button_frame, text="/", **button_style2, command=divide)
btndivide.grid(row=1, column=3, padx=5, pady=5)

btnsubtract = tk.Button(button_frame, text="-", **button_style2, command=subtract)
btnsubtract.grid(row=0, column=4, padx=5, pady=5)

btnmultiply = tk.Button(button_frame, text="*", **button_style2, command=multiply)
btnmultiply.grid(row=1, column=4, padx=5, pady=5)

btnequal = tk.Button(button_frame, text="=", **button_style2, command=equals)
btnequal.grid(row=2, column=3, padx=5, pady=5)

btnreset = tk.Button(button_frame, text="C", **button_style2, command=reset)
btnreset.grid(row=2, column=4, padx=5, pady=5)

button_frame.configure(bg="#be7d7b")

root.mainloop()