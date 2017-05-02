# -*- coding: utf-8 -*-
'''
start_urlsを書き換えたもの
'''

import scrapy


class BricksetSpider(scrapy.Spider):
    name = "brickset1"
    allowed_domains = ["brickset.com"]
    start_urls = ['https://brickset.com/sets/year-2016']

    def parse(self, response):
        pass
