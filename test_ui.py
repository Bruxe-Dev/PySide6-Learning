import sys
from pathlib import Path
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt6.QtGui import QIcon

BASE_DIR = Path(__file__).resolve().parent.parent
image_path = BASE_DIR / "images"/"logo.png"

app = QApplication([])
window = QMainWindow()

window.setWindowIcon(QIcon(str(image_path)))
window.setWindowTitle("LESSON 1")
window.setGeometry(100, 100, 600, 400)

button = QPushButton("CLICK",window)
button.setGeometry(100, 100, 200, 100)

window.show()
app.exec()