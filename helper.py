import requests
from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QListWidget, QPushButton,
    QTextBrowser, QTextEdit, QHBoxLayout, QMessageBox
)
from PySide6.QtCore import Qt
class UrlSelectDialog(QDialog):
  def __init__(self, urls, data_file, parent=None):
    super().__init__(parent)
    
    self.setWindowTitle("选择或删除 URL")
    self.setFixedSize(400, 500)
    self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)
    
    self.selected_url = None
    self.data_file = data_file
    
    self.layout = QVBoxLayout(self)
    
    self.list_widget = QListWidget()
    self.list_widget.addItems(urls)
    self.layout.addWidget(self.list_widget)
    
    button_layout = QHBoxLayout()
    self.layout.addLayout(button_layout)
    
    self.select_button = QPushButton("确定")
    button_layout.addWidget(self.select_button)
    
    self.delete_button = QPushButton("删除")
    self.delete_button.setStyleSheet("background-color: #f44336; color: white;")
    button_layout.addWidget(self.delete_button)
    
    self.select_button.clicked.connect(self.accept)
    self.delete_button.clicked.connect(self.delete_selected_url)
    self.list_widget.itemDoubleClicked.connect(self._handle_double_click)

  def _handle_double_click(self, item):
    self.selected_url = item.text()
    self.accept()
      
  def get_selected_url(self):
    if self.list_widget.currentItem():
      return self.list_widget.currentItem().text()
    return None

  def delete_selected_url(self):
    current_item = self.list_widget.currentItem()
    if not current_item:
      QMessageBox.warning(self, "警告", "请先选择一个 URL 进行删除。")
      return
        
    reply = QMessageBox.question(
        self, 
        "确认删除", 
        f"你确定要删除 '{current_item.text()}' 吗？",
        QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
        QMessageBox.StandardButton.No
    )
    
    if reply == QMessageBox.StandardButton.Yes:
      row = self.list_widget.row(current_item)
      self.list_widget.takeItem(row)
      
      self._save_list_to_file()
      QMessageBox.information(self, "成功", "URL 已删除。")

  def _save_list_to_file(self):
    try:
      updated_urls = []
      for i in range(self.list_widget.count()):
        updated_urls.append(self.list_widget.item(i).text())

      with open(self.data_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(updated_urls))
    except Exception as e:
      QMessageBox.critical(self, "错误", f"保存文件时发生错误：{e}")
def valid_prefix(url:str, terminal:QTextBrowser):
  if url == "":
    terminal.append(f"url不可为空")
    return False
  valid = ["http://", "https://"]
  if not any(url.lower().startswith(prefix) for prefix in valid):
    terminal.append(f"url should start with https:// or http://")
    return False
  return True

def get_body(input:QTextEdit):
  body = {}
  raw_text = input.toPlainText()
  for line in raw_text.splitlines():
    key,value = line.split('=', 1)
    key = key.strip()
    value = value.strip()
    body[key] = int(value)
  return body

def http_request(type:str, url:str, body:dict, check:bool):
  method = getattr(requests, type.lower())
  try:
    res:requests.Response
    if check:
      res = method(url, json=body)
    else:
      res = method(url)
    if res.status_code == 200:
      return {
        'status_code': 200,
        'body':res.json()
        }
    else:
      return {
        'status_code': res.status_code,
        'body':res.text
      }
  except requests.exceptions.RequestException:
    return {
      'status_code': 404,
      'body': "请求失败"
    }
  
def get_saved_url(tp:str):
  path = f"./save/{tp}.txt"
  try:
    with open(path, 'r', encoding='utf-8') as file:
      lines = [line.strip() for line in file]
    return lines
  except FileNotFoundError:
    print(f"错误：文件 '{path}' 未找到。")
    return []
def save_url(url:str, tp:str):
  path = f"./save/{tp}.txt"
  with open(path, 'a', encoding='utf-8') as f:
    f.write(url+'\n')