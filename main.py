from PySide6.QtWidgets import (
  QApplication,
  QPushButton,
  QTextEdit,
  QLineEdit,
  QTextBrowser,
  QComboBox,
  QCheckBox,
  QDialog,
  QWidget,
  QVBoxLayout,
  QListWidget,
  QMainWindow
)
from helper import (
  valid_prefix,
  get_body,
  http_request,
  save_url,
  get_saved_url,
  UrlSelectDialog
)
from ui import Ui_main
from PySide6.QtUiTools import QUiLoader
import sys, os, threading
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
class _MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    mainWidget = QWidget()
    self.ui = Ui_main()
    self.ui.setupUi(mainWidget)
    self.setCentralWidget(mainWidget)
    self.request_body = get_body(self.ui.textEdit)
    self.listener()
  def clear_logger(self):
     self.ui.textBrowser.clear()
  
  def choose_url(self):
    saved_items = get_saved_url("url")
    sub_window = UrlSelectDialog(saved_items, "./save/url.txt", self)
    if sub_window.exec() == QDialog.Accepted:
      url = sub_window.get_selected_url()
      if url:
        self.ui.lineEdit.setText(url)
  def choose_endpoint(self):
    saved_items = get_saved_url("endpoint")
    sub_window = UrlSelectDialog(saved_items, "./save/endpoint.txt", self)
    if sub_window.exec() == QDialog.Accepted:
      endpoint = sub_window.get_selected_url()
      if endpoint:
        self.ui.lineEdit_2.setText(endpoint)
  def save_endpoint(self):
    save_url(self.ui.lineEdit_2.text(), "endpoint")
  def save_url(self):
    save_url(self.ui.lineEdit.text(), "url")
  def thread_request(self):
     thread = threading.Thread(target=self.send_request, args=())
     thread.start()

  def send_request(self):
    url = self.ui.lineEdit.text()
    if not valid_prefix(url, self.ui.textBrowser):
      return
    endpoint = self.ui.lineEdit_2.text()
    type = self.ui.method_list.currentText()
    check = self.ui.checkBox.isChecked()
    res = http_request(type, url+endpoint, self.request_body, check)
    self.ui.textBrowser.append(f"请求已发送至{url+endpoint}")
    self.ui.textBrowser.append(f"响应码: {res['status_code']}\n响应体: {res['body']}")
  def listener(self):
    self.ui.pushButton_4.clicked.connect(self.clear_logger)
    self.ui.pushButton.clicked.connect(self.thread_request)
    self.ui.choose_1.clicked.connect(self.choose_url)
    self.ui.choose_2.clicked.connect(self.choose_endpoint)
    self.ui.save_1.clicked.connect(self.save_url)
    self.ui.save_2s.clicked.connect(self.save_endpoint)
if __name__ == "__main__":
  if not os.path.exists("./save"):
    os.makedirs("./save")
  with open("./save/endpoint.txt", 'a', encoding='utf-8') as f:
        f.write('')
  with open("./save/url.txt", 'a', encoding='utf-8') as f:
        f.write('')
  app = QApplication(sys.argv)
  main = _MainWindow()
  main.show()
  sys.exit(app.exec())