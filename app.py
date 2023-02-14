from data.main import MainWeather, QApplication

import sys

if __name__ == "__main__":

  app = QApplication(sys.argv)

  win = MainWeather()

  win.show()
  app.exec()