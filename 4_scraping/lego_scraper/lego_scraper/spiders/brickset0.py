# -*- coding: utf-8 -*-
'''
リスト4.5
scrapy genspider brickset brickset.com で作成した直後のファイル
'''

import scrapy


class BricksetSpider(scrapy.Spider):
    name = "brickset0"
    allowed_domains = ["brickset.com"]
    start_urls = ['http://brickset.com/']

    def parse(self, response):
        pass
