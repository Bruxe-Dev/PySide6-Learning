from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PyQt6.QtCore import Qt

app = QApplication([])

window = QMainWindow()
window.setWindowTitle("AirSketch")
window.setGeometry(100, 100, 600, 400)

click_count = 0

label = QLabel("Click count: 0", window)
label.setGeometry(150, 100, 300, 50)

def on_button_clicked():
    global click_count  # Allow this function to modify the global variable
    click_count += 1    # Increase the count by 1
    label.setText(f"Click count: {click_count}")  # Update the label text
    print(f"Button clicked! Count: {click_count}")

button = QPushButton("Click Me!", window)
button.setGeometry(200, 200, 200, 80)

button.clicked.connect(on_button_clicked)


window.show()
app.exec()