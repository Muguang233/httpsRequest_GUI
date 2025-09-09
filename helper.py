from PySide6.QtWidgets import (
  QTextBrowser,
  QTextEdit
)
import requests, json
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
  match type:
    case "GET":
      return get_request(type, url, body, check)
    case "POST":
      pass

def get_request(type:str, url:str, body:dict, check:bool):
  try:
    res:requests.Response
    if check:
      res = requests.get(url, json=body)
    else:
      res = requests.get(url)
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
  except requests.exceptions.RequestException as err:
    return {
      'status_code': 404,
      'body': "请求失败"
    }