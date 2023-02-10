import sys

from PyQt6.QtWidgets import (
    QApplication,
    QVBoxLayout,
    QWidget,
    QPushButton,

)

from clients import EmailClient


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(300, 300)
        self.setWindowTitle("Email Manager")

        layout = QVBoxLayout()
        self.setLayout(layout)

        button = QPushButton("Search Email", self)
        button.clicked.connect(self.clicked)
        layout.addWidget(button)

    def clicked(self):
        print("Clicked")
        email = EmailClient()
        email.start()


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
