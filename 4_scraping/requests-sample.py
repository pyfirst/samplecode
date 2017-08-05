# Requestsでgihyo.jpのページのデータを取得

import requests

r = requests.get('http://gihyo.jp')
print(r.status_code)  # ステータスコードを取得
print(r.text[:50])  # 先頭50文字を取得
