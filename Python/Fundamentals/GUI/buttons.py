import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 200, 300, 400) #window geometry
       
        self.label = QLabel("Button still not clicked", self) #created a label text
        self.label.setGeometry(0, 0, 300, 500)
        self.label.setFont(QFont("Consolas"))
        self.label.setStyleSheet("font: 16px;"
                                 "font-weight: bold;" 
                                 "font-background: gray;"
                                 )
        self.label.setAlignment(Qt.AlignHCenter)
        self.label.setAlignment(Qt.AlignVCenter)
        self.initUI() 

    def initUI(self):
        self.button = QPushButton("Click me!", self)    #create button
        self.button.setGeometry(30, 30, 100, 50)        #button geometry
        self.button.setStyleSheet("font-size: 16px;"
                             "color: white;"
                             "font-weight: bold;"
                             "background-color: blue")
        self.button.clicked.connect(self.on_click)                    
    def on_click(self):
        print("Clicked")
        self.button.setText("Clicked")  #override button
        self.label.setText("Ur gay")    #override label
        self.button.setDisabled(True)   #button disabled after clicking

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()