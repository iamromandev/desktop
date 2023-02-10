import sys

from PyQt6.QtWidgets import QApplication, QWidget, QPushButton


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(300, 300)
        self.setWindowTitle("Email Manager")

        button = QPushButton("Search Email", self)
        button.move(100, 100)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())

