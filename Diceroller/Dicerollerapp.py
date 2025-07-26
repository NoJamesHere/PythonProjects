import random, time
import tkinter as tk
from playsound import playsound
import os

number = 0
running = True
dice_faces = {
    1: "⚀",
    2: "⚁",
    3: "⚂",
    4: "⚃",
    5: "⚄",
    6: "⚅"
    }

enabling = input("Do you want to enable sound? (y/n): ").strip().lower()
base_path = os.path.dirname(os.path.abspath(__file__))
sound_path = os.path.join(base_path, "Dicesound.wav")

reset_label_after_id = None
reset_label_after_id2 = None
def rolldice_animation(rolls_left):
    global number, reset_label_after_id, reset_label_after_id2
    if rolls_left > 0:
        number = random.randint(1, 6)
        label.config(text=dice_faces[number], foreground="#f5f5f5")
        root.after(500, rolldice_animation, rolls_left - 1)
        print(number)
    else:
        # Final roll
        number = random.randint(1, 6)
        label.config(text=dice_faces[number])
        if(enabling == "y" and os.path.exists(sound_path)):
            playsound(sound_path, block=False)
        
        if(number == 6):
            label2.config(text="A six! Lucky!")
        elif(number == 1):
            label2.config(text="Too bad!")
        else:
            label2.config(text="Not bad. Could be worse or better")
        if reset_label_after_id is not None:
            root.after_cancel(reset_label_after_id)
        if reset_label_after_id2 is not None:
            root.after_cancel(reset_label_after_id2)
        print(f"Final roll: {number}")
        btnroll.config(state="normal")
        btnroll.config(bg="#a22127")
        reset_label_after_id = root.after(3000, lambda: label2.config(text="Roll the dice!"))
        reset_label_after_id2 = root.after(6000, lambda: label.config(foreground="#a8a5a5"))

def rolldice():
    global reset_label_after_id, reset_label_after_id2
    btnroll.config(state="disabled", bg="#834C43")
    if reset_label_after_id2 is not None:
        root.after_cancel(reset_label_after_id2)
        reset_label_after_id2 = None
    
    if reset_label_after_id is not None:
        root.after_cancel(reset_label_after_id)
        reset_label_after_id = None
    rolldice_animation(9)
    label2.config(text="Rolling..")
    
    

button_style2 = {
    "width": 5,
    "height": 2,
    "font": ("Helvetica", 14, "bold"),
    "bg": "#a22127",
    "fg": "white",
    "activebackground": "#834C43",
    "activeforeground": "white",
    "disabledforeground": "#CCCCCC",
    "bd": 0,
    "highlightthickness": 0,
    "relief": "flat"
}



# --- GUI 
root = tk.Tk()
root.title("Dice Roller")
root.geometry("380x380")
root.configure(bg="#35654d")
label = tk.Label(root, text=dice_faces[1], font=("Helvetica", 28, "bold"),
                 bg="#3a3a3a", fg="#a8a5a5", anchor="center", padx=10)
label.pack(pady=20, fill="x")
label2 = tk.Label(root, text="Roll the dice!", font=("Helvetica", 16, "bold"),
                 bg="#3a3a3a", fg="white", anchor="center", padx=10)
label2.pack(pady=25, fill="x")
button_frame = tk.Frame(root)
button_frame.pack()

btnroll = tk.Button(button_frame, text="Roll", **button_style2, command=rolldice)
btnroll.grid(row=0, column=3, padx=5, pady=5)

button_frame.configure(bg="#d4af37")
root.mainloop()