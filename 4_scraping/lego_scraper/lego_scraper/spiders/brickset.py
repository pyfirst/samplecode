# -*- coding: utf-8 -*-
import scrapy


class BricksetSpider(scrapy.Spider):
    name = "brickset"
    allowed_domains = ["brickset.com"]
    start_urls = ['https://brickset.com/sets/year-2017']

    def parse(self, response):
        for set in response.css('article.set'):
            meta = set.css('div.meta')
            # セット番号を取得
            number = meta.css('h1 span::text').re_first(r'(.+): ')
            # セット名を取得
            name = set.css('div.highslide-caption h1 a::text').extract_first()
            yield {
                'number': number,
                'name': name,
                'theme': meta.css('.tags a')[1].css('a::text').extract_first(),
                'subtheme': meta.css('.tags a.subtheme::text').extract_first(),
                'rating': meta.css('.rating::attr("title")').extract_first(),
            }
        next_url = response.css('li.next a::attr("href")').extract_first()
        if next_url:
            yield scrapy.Request(next_url)
