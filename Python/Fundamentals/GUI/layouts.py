import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout
from PyQt5.QtGui import QFont

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        label1 = QLabel("One")
        label2 = QLabel("Two")
        label3 = QLabel("Three")
        label4 = QLabel("Four")
        label5 = QLabel("Five")

        label1.setStyleSheet("background-color: Red;")
        label2.setStyleSheet("background-color: Yellow;")
        label3.setStyleSheet("background-color: Blue;")
        label4.setStyleSheet("background-color: Green;")
        label5.setStyleSheet("background-color: Orange;")

        vBox = QVBoxLayout()
        vBox.addWidget(label1)
        vBox.addWidget(label2)
        vBox.addWidget(label3)
        vBox.addWidget(label4)
        vBox.addWidget(label5)

        central_widget.setLayout(vBox)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ =="__main__":
    main()