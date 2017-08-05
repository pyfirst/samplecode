# -*- coding: utf-8 -*-
'''
リスト4.9
セット番号を取り出す
'''

import scrapy


class BricksetSpider(scrapy.Spider):
    name = "brickset3"
    allowed_domains = ["brickset.com"]
    start_urls = ['https://brickset.com/sets/year-2016']

    def parse(self, response):
        for brickset in response.css('article.set'):
            meta = brickset.css('div.meta')
            # セット番号を取得
            number = meta.css('h1 span::text').re_first(r'(.+): ')
            # セット名を取得
            name = brickset.css('div.highslide-caption h1::text').extract_first()
            print(number, name)

