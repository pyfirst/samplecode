# Beautiful Soup 4で「技評ねこ部通信」を取得

import requests
from bs4 import BeautifulSoup

r = requests.get('http://gihyo.jp/lifestyle/clip/01/everyday-cat')
soup = BeautifulSoup(r.content, 'html.parser')
title = soup.title  # titleタグの情報を取得

print(type(title))  # オブジェクトの型は Tag 型
# <class 'bs4.element.Tag'>

print(title)  # タイトルの中身を確認
# <title>技評ねこ部通信｜gihyo.jp … 技術評論社</title>

print(title.text)  # タイトルの中のテキストを取得
# 技評ねこ部通信｜gihyo.jp … 技術評論社

div = soup.find('div', class_='readingContent01')
for li in div.find_all('li'):  # divタグの中の全liタグを取得
    url = li.a['href']
    date, text = li.a.text.split()
    print('{},{},{}'.format(date, text, url))
