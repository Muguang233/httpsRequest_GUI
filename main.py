from PySide6.QtWidgets import (
  QApplication,
  QPushButton,
  QTextEdit,
  QLineEdit,
  QTextBrowser,
  QComboBox,
  QCheckBox
)
from helper import (
  valid_prefix,
  get_body,
  http_request
)
from PySide6.QtUiTools import QUiLoader
import sys

class Mainwindow():
  def __init__(self):
    super().__init__()
    self.window = QUiLoader().load('./ui/req.ui')
    self.request_body = get_body(self.window.findChild(QTextEdit, "textEdit"))
    self.logger = self.window.findChild(QTextBrowser, "textBrowser")
    self.listener()
  def choose_url(self):
    pass
  def send_request(self):
    url = self.window.findChild(QLineEdit, "lineEdit").text()
    if not valid_prefix(url, self.logger):
      return
    endpoint = self.window.findChild(QLineEdit, "lineEdit_2").text()
    type = self.window.findChild(QComboBox, "method_list").currentText()
    check = self.window.findChild(QCheckBox, "checkBox").isChecked()
    res = http_request(type, url+endpoint, self.request_body, check)
    self.logger.append(f"请求已发送至{url+endpoint}")
    self.logger.append(f"响应码: {res['status_code']}\n响应体: {res['body']}")
  def clear_logger(self):
    self.logger.clear()
  def listener(self):
    self.window.findChild(QPushButton, "pushButton_4").clicked.connect(self.clear_logger)
    self.window.findChild(QPushButton, "pushButton").clicked.connect(self.send_request)
    self.window.findChild(QPushButton, "choose_1").clicked.connect(self.choose_url)

if __name__ == "__main__":
  app = QApplication(sys.argv)
  main = Mainwindow()
  main.window.show()
  sys.exit(app.exec())