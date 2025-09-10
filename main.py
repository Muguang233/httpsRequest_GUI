from PySide6.QtWidgets import (
  QApplication,
  QPushButton,
  QTextEdit,
  QLineEdit,
  QTextBrowser,
  QComboBox,
  QCheckBox,
  QDialog,
  QVBoxLayout,
  QListWidget
)
from helper import (
  valid_prefix,
  get_body,
  http_request,
  save_url,
  get_saved_url,
  UrlSelectDialog
)
from PySide6.QtUiTools import QUiLoader
import sys, os
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class Mainwindow():
  def __init__(self):
    super().__init__()
    path = resource_path('ui/req.ui')
    self.window = QUiLoader().load(path)
    self.request_body = get_body(self.window.findChild(QTextEdit, "textEdit"))
    self.logger = self.window.findChild(QTextBrowser, "textBrowser")
    self.listener()
  def choose_url(self):
    saved_items = get_saved_url("url")
    sub_window = UrlSelectDialog(saved_items, "./save/url.txt", self.window)
    if sub_window.exec() == QDialog.Accepted:
      url = sub_window.get_selected_url()
      if url:
        self.window.findChild(QLineEdit, "lineEdit").setText(url)
  def choose_endpoint(self):
    saved_items = get_saved_url("endpoint")
    sub_window = UrlSelectDialog(saved_items, "./save/endpoint.txt", self.window)
    if sub_window.exec() == QDialog.Accepted:
      endpoint = sub_window.get_selected_url()
      if endpoint:
        self.window.findChild(QLineEdit, "lineEdit_2").setText(endpoint)
  def save_endpoint(self):
    save_url(self.window.findChild(QLineEdit, "lineEdit_2").text(), "endpoint")
  def save_url(self):
    save_url(self.window.findChild(QLineEdit, "lineEdit").text(), "url")
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
    self.window.findChild(QPushButton, "choose_2").clicked.connect(self.choose_endpoint)
    self.window.findChild(QPushButton, "save_1").clicked.connect(self.save_url)
    self.window.findChild(QPushButton, "save_2s").clicked.connect(self.save_endpoint)
if __name__ == "__main__":
  if not os.path.exists("./save"):
    os.makedirs("./save")
  with open("./save/endpoint.txt", 'a', encoding='utf-8') as f:
        f.write('')
  with open("./save/url.txt", 'a', encoding='utf-8') as f:
        f.write('')
  app = QApplication(sys.argv)
  main = Mainwindow()
  main.window.show()
  sys.exit(app.exec())