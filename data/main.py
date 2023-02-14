from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QTextEdit
from PyQt6 import QtCore
from PyQt6.QtGui import QIcon,QPixmap
from data.getwether import get_weather

class MainWeather(QMainWindow):
  def __init__(self, width=500, height=500, title="Weather app"):
    super().__init__()
    self.setWindowTitle(title)
    self.setGeometry(500, 250, width, height)
    icon_title = QIcon("image\icon_title.png")
    far_icon = QIcon("image//f.png")
    tempe = QPixmap("image//temperature.png").scaled(QtCore.QSize(70, 70))
    self.setWindowIcon(icon_title)
    self.fbutton = QPushButton(far_icon," Farg'ona",self)
    self.temp_img = QLabel(self)
    self.temp_img.setPixmap(tempe)
    self.temp_img.setGeometry(300, 160, 150, 150)
    self.fbutton.setGeometry(width//2, 20, 150, 50)
    self.temp = QLabel("Harorat",self)
    self.temp.setGeometry(20, 200, 150, 50)
    self.fbutton.clicked.connect(self.far_temp) 
    self.fbutton.setStyleSheet("QPushButton { background-color: yellow }")
    self.setStyleSheet("background-color: red")
  
  def far_temp(self):
    temp = get_weather(city="фергана")
    self.temp.setText("Harorat: "+temp)


