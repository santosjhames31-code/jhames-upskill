import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QRadioButton, QLabel, QButtonGroup
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(500, 100, 500, 500)

        self.label1 = QLabel("Variant", self)   #labels
        self.label2 = QLabel("Storage", self)

        self.radio1 = QRadioButton("Iphone 13", self) #initialized radio buttons
        self.radio2 = QRadioButton("Iphone 14", self)
        self.radio3 = QRadioButton("Iphone 15", self) 
        self.radio4 = QRadioButton("64 GB", self)
        self.radio5 = QRadioButton("128 GB", self)
        self.radio6 = QRadioButton("256 GB", self)

        self.group1 = QButtonGroup(self) #created groups
        self.group2 = QButtonGroup(self)

        self.initUI()

    def initUI(self):        

        self.label1.setGeometry(10, 0, 300, 50) #pos and geometry l1
        self.label1.setAlignment(Qt.AlignCenter)
        self.radio1.setGeometry(10, 50, 300, 50) 
        self.radio2.setGeometry(10, 100, 300, 50)
        self.radio3.setGeometry(10, 150, 300, 50)

        self.label2.setGeometry(10, 200, 300, 50) #pos and geometry l2
        self.label2.setAlignment(Qt.AlignCenter)

        self.radio4.setGeometry(10, 250, 300, 50)
        self.radio5.setGeometry(10, 300, 300, 50)
        self.radio6.setGeometry(10, 350, 300, 50)

        self.group1.addButton(self.radio1) #added buttons 1, 2, and 3 to group 1 
        self.group1.addButton(self.radio2)
        self.group1.addButton(self.radio3)
        
        self.group2.addButton(self.radio4) #added buttons 4, 5, and 6 to group 2 
        self.group2.addButton(self.radio5)
        self.group2.addButton(self.radio6)
        
        self.setStyleSheet(
                    "QLabel{"
                    "color: black;"
                    "font-weight: bold;"
                    "font-size: 20px;"
                    "background-color: red;"
                    "}"
                    "QRadioButton{"
                    "font-size: 20px;"
                    "background-color: blue;"
                    "color: white;"
                    "padding: 10px;"
                    "}")

        self.radio1.toggled.connect(self.radio_button_changed)
        self.radio2.toggled.connect(self.radio_button_changed)
        self.radio3.toggled.connect(self.radio_button_changed)
        self.radio4.toggled.connect(self.radio_button_changed)
        self.radio5.toggled.connect(self.radio_button_changed)
        self.radio6.toggled.connect(self.radio_button_changed)

    def radio_button_changed(self):
        radio_sender = self.sender()
        if radio_sender.isChecked():
            print(f"{radio_sender.text()} is selected")

        
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()