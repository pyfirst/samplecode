# 概要

このソースコードは、[Pythonエンジニア ファーストブック](http://gihyo.jp/book/2017/978-4-7741-9222-2)の第6章（Webアプリケーション開発）のレゴ管理アプリケーションのサンプルソースです。ぜひこ活用ください。

## レゴ管理アプリケーション

アプリケーションは以下の手順を行うと動作を確認できます。

```
$ git clone git@github.com:pyfirst/samplecode.git
$ cd samplecode/6_web/
$ python3 -m venv env # 仮想環境を作成
$ . env/bin/activate # 仮想環境を有効化
(env) $ pip install -r requirements.txt # Djangoのインストール
(env) $ cd brickset_app/ アプリケーションのディレクトリに移動
(env) $ python manage.py migrate # DBのマイグレーションを実行
(env) $ python manage.py import_item # DBへマスターデータを挿入
(env) $ python manage.py createsuperuser # 管理者ユーザーの作成
(env) $ python manage.py runserver # 開発サーバーの起動
```

開発サーバーを起動したら、http://127.0.0.1:8000/item/ にアクセスしてください。
