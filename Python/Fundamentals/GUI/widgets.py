import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon, QFont

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Jhamestzy")
        self.setGeometry(700, 200, 300, 200)
        self.setWindowIcon(QIcon("images.png"))

        label = QLabel("Hello Wolrd", self)
        label.setFont(QFont("Consolas", 20))
        label.setGeometry(0, 0, 500, 100)
        label.setStyleSheet("color: Blue;"
                            "background-color: Red;"
                            "font-weight: bold;"
                            "font-style: italic;"
                            "text-decoration: underline;"
                            )


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()