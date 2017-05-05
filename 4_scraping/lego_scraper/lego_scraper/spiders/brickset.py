# -*- coding: utf-8 -*-
'''
完成形: XPathでピース数、ミニフィグ数、価格を取得する
'''

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
            yield {
                'number': number,
                'name': name,
                'image': brickset.css('img::attr(src)').re_first('(.*)\?'),
                'theme': meta.css('.tags a')[1].css('a::text').extract_first(),
                'subtheme': meta.css('.tags a.subtheme::text').extract_first(),
                'year': meta.css('a.year::text').extract_first(),
                'rating': meta.css('.rating::attr(title)').extract_first(),
                'pieces': meta.xpath('.//dt[text()="Pieces"]/following-sibling::dd').css('::text').extract_first(),
                'minifigs': meta.xpath('.//dt[text()="Minifigs"]/following-sibling::dd').css('::text').extract_first(),
                'us_price': price.re_first('\$([\d+\.\d+]+)'),
                'eu_price': price.re_first('([\d+\.\d+]+)€'),
                'owner': brickset.css('dl.admin dd').re_first('(\d+) own this set'),
                'want_it': brickset.css('dl.admin dd').re_first('(\d+) want it'),
            }
        # 次のページを取得する
        next_url = response.css('li.next a::attr(href)').extract_first()
        if next_url:
            yield scrapy.Request(next_url)

