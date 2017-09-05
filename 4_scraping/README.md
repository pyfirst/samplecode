# 第4章 スクレイピング

「第4章 スクレイピング」のサンプルコードです。

以下のフォルダ、ファイルがあります。

* lego_scraper/: LEGOデータをスクレイピングするコードが入ったフォルダ
* 4_2_scraping.ipynb: 「4.2 サードパーティ製パッケージを使ってスクレイピングに挑戦」のコードを記述した Jupyter Notebook
* bs4-sample.py: Beautiful Soup 4で「技評ねこ部通信」を取得するコード
* requests-json.py: RequestsでJSONを取得するコード
* requests-sample.py: Requestsのコード
* requirements.txt: 4章で使用するライブラリをインストールするための requirements.txt

## lego_scraper について

`lego_scraper/lego_scraper/spiders` の下に、各手順での Spider のコードが入っています。
書籍の対応する場所は、コード中に `リスト4.5` のように記述してあります。

以下の手順で Spider が手元で実行できます。

```
$ git clone git@github.com:pyfirst/samplecode.git
$ cd samplecode/4_scraping/lego_scraper
$ python3 -m venv env # 仮想環境を作成
$ . env/bin/activate # 仮想環境を有効化
(env) $ pip install scrapy # scarpy をインストール
(env) $ scrapy crawl brickset0.py # 最初の手順の Spider を実行
(env) $ scrapy crawl brickset1.py
:
(env) $ scrapy crawl brickset.py # 完成形の Spider を実行
```