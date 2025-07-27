from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QVBoxLayout, QCheckBox
import sys

app = QApplication(sys.argv)  # 1. Create the app
window = QWidget()            # 2. Create a window
window.setWindowTitle("Hello PyQt")
window.setGeometry(100, 100, 400, 300)

welcome = "Hello!"

label = QLabel(welcome, parent=window)

button = QPushButton("Click Me", parent=window)

check = QCheckBox("Todo", parent=window)

def on_click():
    label.setText("You clicked me.. Why..")

button.clicked.connect(on_click)


layout = QVBoxLayout()

layout.addWidget(label)
layout.addWidget(button)
layout.addWidget(check)

def checkbox_changed():
    if check.isChecked():
        label.setText("You checked the box!")
    else:
        label.setText(welcome)
check.stateChanged.connect(checkbox_changed)
window.setLayout(layout)


window.setStyleSheet("background-color: #2e2e2e; color: white;")  # Set background color and text color
window.show()                 # 3. Show the window
sys.exit(app.exec())          # 4. Run the app loop