import json

from django.core.management.base import BaseCommand

from ...models import Item


# BaseCommandを継承して作成
class Command(BaseCommand):
    # python manage.py help import_itemで表示されるメッセージ
    help = 'Create Item from json file'

    def remove_null(self, value, default):
        if value is None:
            return default
        return value

    # コマンドが実行された際に呼ばれるメソッド
    def handle(self, *args, **options):

        # ファイルのオープン
        with open('web.json', 'r') as file:

            # JSONの読み込み
            data = json.load(file)
            count = 0

            # 取得したデータを1件づつ取り出す
            for item_obj in data:

                if not item_obj['number']:
                    continue

                # Itemの保存処理
                item = Item()
                item.set_number = item_obj['number']
                item.name = self.remove_null(item_obj['name'], '')
                item.image_url = self.remove_null(item_obj['image'], '')
                item.rate = self.remove_null(item_obj['rating'], 0.0)
                item.piece_count = self.remove_null(item_obj['pieces'], 0)
                item.minifig_count = self.remove_null(item_obj['minifigs'], 0)
                item.us_price = self.remove_null(item_obj['us_price'], 0.0)
                item.want_it_count = self.remove_null(item_obj['want_it'], 0)
                item.owner_count = self.remove_null(item_obj['owner'], 0)
                item.save()

                count += 1
                print('Create Item: {0}: {1}'.format(item.id, item.name))

            print('{} items have been created.'.format(count))
