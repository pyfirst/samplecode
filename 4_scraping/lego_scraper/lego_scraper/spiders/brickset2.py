# -*- coding: utf-8 -*-
'''
リスト4.8
セット名称を取り出す
'''

import scrapy


class BricksetSpider(scrapy.Spider):
    name = "brickset2"
    allowed_domains = ["brickset.com"]
    start_urls = ['https://brickset.com/sets/year-2016']

    def parse(self, response):
        for brickset in response.css('article.set'):
            print(brickset.css('div.highslide-caption h1::text').extract_first())
