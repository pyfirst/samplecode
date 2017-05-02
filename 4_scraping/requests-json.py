import requests

r = requests.get('https://connpass.com/api/v1/event/?keyword=python')
data = r.json() # JSONをデコードしたデータを取得
for event in data['events']:
    print(event['title'])
