# -*- coding: utf-8 -*-
import scrapy


class BricksetSpider(scrapy.Spider):
    name = "brickset"
    allowed_domains = ["brickset.com"]
    start_urls = ['https://brickset.com/sets/year-2016']

    def parse(self, response):
        for brickset in response.css('article.set'):
            meta = brickset.css('div.meta')
            # セット番号を取得
            number = meta.css('h1 span::text').re_first(r'(.+): ')
            # セット名を取得
            name = brickset.css('div.highslide-caption h1 a::text').extract_first()
            price = meta.xpath('.//dt[text()="RRP"]/following-sibling::dd/text()')
            us_price = price.re_first('\$([\d+\.\d+]+)')
            eu_price = price.re_first('([\d+\.\d+]+)€')
            yield {
                'number': number,
                'name': name,
                'image': brickset.css('img ::attr(src)').re_first('(.*)\?'),
                'theme': meta.css('.tags a')[1].css('a::text').extract_first(),
                'subtheme': meta.css('.tags a.subtheme::text').extract_first(),
                'rating': meta.css('.rating::attr("title")').extract_first(),
                'pieces': meta.xpath('.//dt[text()="Pieces"]/following-sibling::dd/a/text()').extract_first(),
                'minifigs': meta.xpath('.//dt[text()="Minifigs"]/following-sibling::dd/a/text()').extract_first(),
                'us_price': us_price,
                'eu_price': eu_price,
            }
        next_url = response.css('li.next a::attr("href")').extract_first()
        if next_url:
            yield scrapy.Request(next_url)
