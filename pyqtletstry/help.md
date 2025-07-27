##### File writting by AI

🎓 PYQT 101 — THE FULL STARTER CLASS
🧠 WHAT IS PYQT?
PyQt is a Python wrapper for the Qt Framework, which is a super powerful C++ GUI toolkit used to build desktop applications. PyQt lets you access all those features using Python.

So if you’ve ever thought:

"I want a program with windows, buttons, checkboxes, sliders, dialogs, tabs, and pop-ups…”

PyQt is your toolkit.

You write Python 🐍
It gives you native-looking desktop apps on Windows, Mac, and Linux 💻

🧰 INSTALLING PYQT
You can pick PyQt5 or PyQt6 — I recommend PyQt6 (it's newer).

bash

pip install PyQt6
Optional dev tool (highly recommended):

bash

pip install pyqt6-tools
That gives you access to Qt Designer, a visual GUI builder (drag & drop UI editor).

🔧 THE BASIC PYQT APP STRUCTURE
Here’s what every PyQt app looks like at the core:

python

import sys
from PyQt6.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)  # 1. Create the app
window = QWidget()            # 2. Create a window
window.setWindowTitle("Hello PyQt")
window.resize(300, 200)
window.show()                 # 3. Show the window
sys.exit(app.exec())          # 4. Run the app loop
🧠 Breakdown:
QApplication: Core app object — handles events, mouse, keyboard.

QWidget: The base class for all UI elements (buttons, labels, windows, etc.).

.exec(): Starts the app loop — PyQt apps are event-driven.

🪟 ADDING UI ELEMENTS (WIDGETS)
Let's throw in a label and a button:

python

from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton

app = QApplication([])

window = QWidget()
window.setWindowTitle("Assistant Vibes")
window.setGeometry(100, 100, 400, 300)

label = QLabel("Hey James 👋", parent=window)
label.move(50, 50)

button = QPushButton("Click Me", parent=window)
button.move(50, 100)

window.show()
app.exec()
➕ Wanna make the button do something?
python

def on_click():
    label.setText("You clicked me 😎")

button.clicked.connect(on_click)
📐 LAYOUTS (no hardcoding positions)
Instead of .move() for every widget, you use layouts:

python

from PyQt6.QtWidgets import QVBoxLayout

layout = QVBoxLayout()
layout.addWidget(label)
layout.addWidget(button)
window.setLayout(layout)
You can use:

QVBoxLayout() = vertical layout

QHBoxLayout() = horizontal layout

QGridLayout() = grid/row/column style

QFormLayout() = for form-style apps (labels + fields)

📋 COMMON WIDGETS
Widget	What it does
QLabel	Display text or images
QPushButton	Clickable button
QLineEdit	Text input field
QTextEdit	Multiline input
QCheckBox	Checkbox
QRadioButton	Radio option
QComboBox	Dropdown menu
QSlider	Slider bar
QProgressBar	Progress indicator
QListWidget	List of items
QTableWidget	Spreadsheet-style table

🧠 SIGNALS & SLOTS (Events)
PyQt uses the signals and slots system.

A signal = "something happened"

A slot = "a function that runs when that happens"

python

button.clicked.connect(your_function)
You can also create custom signals later when you're building bigger apps.

🖼️ DESIGNER MODE (GUI BUILDER)
Run Qt Designer:

bash

pyqt6-tools designer
Drag and drop widgets (buttons, sliders, etc.)

Save it as .ui file.

Convert to Python:

bash

pyuic6 yourfile.ui -o yourfile.py
Now you can import it into your main script and work with it.

🧰 PUTTING IT ALL TOGETHER — SIMPLE ASSISTANT APP
python

from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
import sys
import random

quotes = [
    "You did the right thing blocking him 🧱",
    "You're healing. Don't look back 👑",
    "You're in your revenge arc 😤",
    "Let them miss you in silence 🕊️",
]

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("L.E.E. Lite")
window.resize(400, 200)

layout = QVBoxLayout()

label = QLabel("Ready for your quote, king?")
button = QPushButton("Give me wisdom")

def show_quote():
    label.setText(random.choice(quotes))

button.clicked.connect(show_quote)

layout.addWidget(label)
layout.addWidget(button)

window.setLayout(layout)
window.show()

sys.exit(app.exec())
🛠️ WHERE TO GO NEXT
Build a real mood tracker

Turn it into a journaling assistant

Add text-to-speech using pyttsx3

Add GPT API to respond with AI wisdom

Add system tray icon

Or even turn it into a taskbar productivity buddy

📚 BONUS LEARNING RESOURCES
Resource	Link
PyQt6 Docs	https://doc.qt.io/qtforpython-6/
ZetCode PyQt Tutorial	https://zetcode.com/gui/pyqt6/
Real Python PyQt Guide	https://realpython.com/python-pyqt-gui-calculator/

