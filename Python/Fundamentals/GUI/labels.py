import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QFont #for fontstyle and size
from PyQt5.QtCore import Qt #for font alignment

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(500, 500, 500, 500)

        label = QLabel("Frenz Alfie", self)
        label.setFont(QFont("Times New Roman", 12))
        label.setGeometry(10, 10, 120, 60)
        label.setStyleSheet("color: blue;"
                            "background-color: green;"
                            "font-weight: bold;"
                            "text-decoration: underline;")

        label.setAlignment(Qt.AlignTop)
        label.setAlignment(Qt.AlignVCenter)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()