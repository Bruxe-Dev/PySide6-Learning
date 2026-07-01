from pathlib import Path
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt6.QtGui import QIcon

app = QApplication([])

BASE_DIR = Path(__file__).resolve().parent
image = BASE_DIR / "images" / "logo.png"

print(image)
print(image.exists())

icon = QIcon(str(image))
print(icon.isNull())

app.setWindowIcon(icon)

window = QMainWindow()
window.setWindowTitle("LESSON 1")
window.setGeometry(100, 100, 600, 400)
window.setWindowIcon(icon)

button = QPushButton("CLICK", window)
button.setGeometry(200, 150, 200, 100)

window.show()
app.exec()