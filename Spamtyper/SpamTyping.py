import pyautogui
import time
from plyer import notification

TextToType = input("What do you want to type?\n")
Running = True

while Running:
    NumberOfTexts = input("How many lines do you want to type? ")

    if not NumberOfTexts.isdigit():
        print("Please enter an valid number")
        continue
    else:
        NumberOfTexts = int(NumberOfTexts)
        print("\n\n\nPlease continue by entering your designated space to spam type it in.\nIt will start in a quick moment..")
        print("⚠️ Press Ctrl+C to cancel before it starts.")
        time.sleep(10)
        for i in range(NumberOfTexts):
            pyautogui.write(TextToType, interval=0.1)
            pyautogui.press("enter")
        print(f"\nPrinted your text '{TextToType}' {NumberOfTexts} times.\nGoodbye.")
        notification.notify(
            title="Spam Typer",
            message="The text has been typed out!",
            timeout=10
        )
        Running = False

