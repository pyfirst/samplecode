# -*- coding: utf-8 -*-
'''
セット名称を取得する
'''

import scrapy


class BricksetSpider(scrapy.Spider):
    name = "brickset2"
    allowed_domains = ["brickset.com"]
    start_urls = ['https://brickset.com/sets/year-2016']

    def parse(self, response):
        for brickset in response.css('article.set'):
            print(brickset.css('div.highslide-caption h1 a::text').extract_first())
