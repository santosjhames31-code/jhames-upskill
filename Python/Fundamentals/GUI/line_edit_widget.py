import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)

        self.text_box = QLineEdit(self)
        self.button = QPushButton("Submit", self)

        self.initUI()
        
    def initUI(self):
        self.text_box.setGeometry(10, 10, 200, 50)
        self.button.setGeometry(210, 10, 75, 50)
        self.text_box.setPlaceholderText("Enter your name")
        self.text_box.setStyleSheet("font-family: Consolas;"
                                    "font-size: 24px")
        self.button.clicked.connect(self.submit)
        
    def submit(self):
        text = self.text_box.text()
        print(f"HI {text}")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()