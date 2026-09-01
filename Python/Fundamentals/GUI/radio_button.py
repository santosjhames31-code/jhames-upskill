import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QRadioButton, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(500, 100, 500, 500)

        label = QLabel("Babalikan ko ba siya?", self)
        label.setGeometry(50, 20, 300, 50)
        label.setStyleSheet("color: black;"
                            "font-weight: bold;"
                            "font-size: 20px;")
        self.initUI()
        
    def initUI(self):        
        radio1 = QRadioButton("Ayaw niya na", self)
        radio1.setGeometry(50, 60, 300, 50)
        radio1.setStyleSheet("font-size: 20px;"
                             "background-color: blue;" 
                             "color: white;")
        
        radio2 = QRadioButton("Hindi", self)
        radio2.setGeometry(50, 100, 300, 50)
        radio2.setStyleSheet("font-size: 20px;"
                                     "background-color: blue;" 
                                     "color: white;")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()