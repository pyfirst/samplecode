# -*- coding: utf-8 -*-
'''
次のページを取得する
'''

import scrapy


class BricksetSpider(scrapy.Spider):
    name = "brickset5"
    allowed_domains = ["brickset.com"]
    start_urls = ['https://brickset.com/sets/year-2016']

    def parse(self, response):
        for brickset in response.css('article.set'):
            meta = brickset.css('div.meta')
            # セット番号を取得
            number = meta.css('h1 span::text').re_first(r'(.+): ')
            # セット名を取得
            name = brickset.css('div.highslide-caption h1 a::text').extract_first()
            yield {
                'number': number,
                'name': name,
            }
        # 次のページを取得する
        next_url = response.css('li.next a::attr(href)').extract_first()
        if next_url:
            yield scrapy.Request(next_url)

