from PySide6.QtWidgets import (
  QApplication
)
from PySide6.QtUiTools import QUiLoader
import sys

class Mainwindow():
  def __init__(self):
    super().__init__()
    self.window = QUiLoader().load('./ui/req.ui')

if __name__ == "__main__":
  app = QApplication(sys.argv)
  main = Mainwindow()
  main.window.show()
  sys.exit(app.exec())