# Pythonエンジニア ファーストブックのサンプルコード

```sh
$ python3 -m venv env
$ . env/bin/activate
(env) $ pip install -r requirements.txt
```

## 4_scraping

```sh
(env) $ cd 4_scraping/lego_scraper
(env) $ scrapy crawl brickset -o brickset2016.json
(env) $ scrapy crawl brickset -o brickset2016.csv
```
