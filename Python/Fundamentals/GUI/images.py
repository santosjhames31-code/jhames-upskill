import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(10, 50, 500, 500)

        label = QLabel(self)                #creates label obj
        label.setGeometry(0, 0, 200, 200)       

        pixmap = QPixmap("images.png")       #create pixmap obj
        label.setPixmap(pixmap)               

        label.setScaledContents(True)        #scale geometry to full size
        
        label.setGeometry((self.width() - label.width()) // 2, 
                          (self.height() - label.height()) // 2,   #Center align
                          label.width(), 
                          label.height())
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()