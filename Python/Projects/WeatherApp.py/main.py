import sys
import requests
from datetime import datetime
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QLineEdit, QVBoxLayout, QHBoxLayout, QGraphicsDropShadowEffect
from PyQt5.QtGui import QIcon, QFontDatabase, QFont, QColor, QPalette
from PyQt5.QtCore import Qt


class Menu(QWidget):
    api_key = "ef1f1e1e7b15aa8ba7a7ef805692f853"

    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon("icon.png"))
        now = datetime.now()

        self.title = QLabel("Sinag☀️", self)
        self.day = QLabel(now.strftime("%A"), self)
        self.date = QLabel(now.strftime("%b %d, %Y"), self)
        self.search_bar = QLineEdit(self)
        self.search_bar.setPlaceholderText("Search Location")
        self.submit_button = QPushButton("Done", self)
        self.weather = QLabel("--", self)
        self.temperature = QLabel("--", self)

        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()
        vbox.setContentsMargins(30, 30, 30, 30)
        vbox.setSpacing(12)
        vbox.setAlignment(Qt.AlignCenter)

        vbox.addWidget(self.title, alignment=Qt.AlignCenter)
        vbox.addWidget(self.day, alignment=Qt.AlignCenter)
        vbox.addWidget(self.date, alignment=Qt.AlignCenter)

        vbox.addSpacing(20)

        search_row = QHBoxLayout()
        search_row.setSpacing(5)
        search_row.addWidget(self.search_bar)
        search_row.addWidget(self.submit_button)
        vbox.addLayout(search_row)

        vbox.addSpacing(20)

        vbox.addWidget(self.weather, alignment=Qt.AlignCenter)
        vbox.addWidget(self.temperature, alignment=Qt.AlignCenter)

        self.setLayout(vbox)

        # widget
        self.setGeometry(700, 300, 500, 500)
        self.setWindowTitle("Sinag")

        # font
        font_id = QFontDatabase.addApplicationFont("Coolvetica Rg.otf")
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]

        # alignment
        self.day.setAlignment(Qt.AlignCenter)
        self.date.setAlignment(Qt.AlignCenter)
        self.weather.setAlignment(Qt.AlignCenter)
        self.temperature.setAlignment(Qt.AlignCenter)

        # keep labels transparent
        for label in (self.title, self.day, self.date, self.weather, self.temperature):
            label.setStyleSheet("background: transparent;")

        # style
        self.title.setFont(QFont(font_family, 32))
        self.day.setFont(QFont(font_family, 24))
        self.date.setFont(QFont(font_family, 12))
        self.weather.setFont(QFont(font_family, 24))
        self.temperature.setFont(QFont(font_family, 24))
        self.search_bar.setFont(QFont(font_family, 24))
        self.submit_button.setFont(QFont(font_family, 14))

        # search bar
        self.search_bar.setAlignment(Qt.AlignCenter)
        self.search_bar.setStyleSheet(
            "background: white;"
            "border-radius: 5px;"
            "padding: 5px;"
        )

        # set both text and placeholder colors via palette
        search_palette = self.search_bar.palette()
        search_palette.setColor(QPalette.Text, QColor("#000000"))
        search_palette.setColor(QPalette.PlaceholderText, QColor("#9E9999"))
        self.search_bar.setPalette(search_palette)

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(15)
        shadow.setXOffset(0)
        shadow.setYOffset(3)
        shadow.setColor(QColor(0, 0, 0, 100))
        self.search_bar.setGraphicsEffect(shadow)

        self.setStyleSheet(
            "border-radius: 5px;"
            "background: qlineargradient("
            "x1:0, y1:0, x2:0, y2:1,"
            "stop:0 #a8d8f0, stop:1 #d6ecfa"
            ");"
        )

        # submit button
        self.submit_button.setStyleSheet(
            "background-color: #a8d8f0;"
            "border-radius: 5px;"
            "padding: 8px 16px;"
        )

        button_shadow = QGraphicsDropShadowEffect()
        button_shadow.setBlurRadius(15)
        button_shadow.setXOffset(0)
        button_shadow.setYOffset(3)
        button_shadow.setColor(QColor(0, 0, 0, 100))
        self.submit_button.setGraphicsEffect(button_shadow)

        # match submit_button height to search_bar height
        self.submit_button.setFixedHeight(self.search_bar.sizeHint().height())

        # connect to the get_weather func
        self.submit_button.clicked.connect(self.get_weather)
        self.setFocus()

    def get_coordinates(self):
        url = "http://api.openweathermap.org/geo/1.0/direct"
        params = {
            "q": self.search_bar.text(),
            "limit": 1,
            "appid": self.api_key
        }
        response = requests.get(url, params=params)
        data = response.json()
        if not data:
            return None, None
        return data[0]["lat"], data[0]["lon"]

    def fetch_weather_data(self, lat, lon):
        url = "https://api.openweathermap.org/data/2.5/weather"
        params = {
            "lat": lat,
            "lon": lon,
            "appid": self.api_key,
            "units": "metric"
        }
        response = requests.get(url, params=params)
        return response.json()

    def get_weather(self):
        lat, lon = self.get_coordinates()
        if lat is None:
            self.weather.setText("City not found")
            self.temperature.setText("")
            print("Location not found")
            return

        weather_data = self.fetch_weather_data(lat, lon)
        condition = weather_data["weather"][0]["main"]
        temp = weather_data["main"]["temp"]

        self.weather.setText(condition)
        self.temperature.setText(f"{round(temp)}C")
        print(condition, temp)


def main():
    app = QApplication(sys.argv)
    menu = Menu()
    menu.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()