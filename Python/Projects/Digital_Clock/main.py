import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QGraphicsDropShadowEffect 
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtGui import QFont, QFontDatabase

class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label = QLabel(self)
        self.timer = QTimer(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("DigiClock")
        self.setGeometry(600, 400, 400, 150)

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)

        self.time_label.setAlignment(Qt.AlignCenter)

        self.time_label.setStyleSheet("""
            font-size: 120px;
            font-weight: bold;
            color: #fafafa;
        """)

        self.setStyleSheet("""
            QWidget {
                background: qlineargradient(
                x1:0, y1:0, x2:1, y2:1,
                stop:0 #1e3c72,
                stop:1 #2a5298
                );
            }
        """)

        font = QFontDatabase.addApplicationFont("SFPRODISPLAYREGULAR.OTF")
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)
        self.update_time()

    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss AP")
        self.time_label.setText(current_time)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())