import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox
from PyQt5.QtCore import Qt
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 200, 300, 200)
        self.checkbox = QCheckBox("Do you like chinitas?", self)
        self.initUI()

    def initUI(self):
        self.checkbox.setStyleSheet("font-size: 14px;"
                                    "font-family: consolas;"
                                    "background-color: blue;"
                                    "font-weight: bold;"
                                    "color: white;")
        self.checkbox.setGeometry(5, 5, 200, 50)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()