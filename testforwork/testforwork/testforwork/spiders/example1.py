# -*- coding: utf-8 -*-
import scrapy


class Example1Spider(scrapy.Spider):
    name = 'example1'
    allowed_domains = ['rewardhospitality.com.au']
    page_number = 2
    start_urls = ['https://www.rewardhospitality.com.au/search?ProductSearch=FRIDGE&PageProduct=1']

    def parse(self, response):
        products = response.css('.product ')
        for product in products:
            title = product.css('.widget-productlist-title  ::text').extract()
            price = product.css('.item-price::text').extract()
            product_code = product.css('.widget-productlist-code  ::text').extract()
            yield {'Title': title, 'Price': price,'product_code':product_code}
        # text = response.css('.widget-productlist-title  ::text').extract()
        # for a in text:
        #     yield {'Name': a}
        # text = response.css('.item-price::text').extract()
        # for a in text:
        #     yield {'Title': a}
        next_page = 'https://www.rewardhospitality.com.au/search?ProductSearch=FRIDGE&PageProduct=' + str(
            Example1Spider.page_number)
        if Example1Spider.page_number < 20:
            Example1Spider.page_number += 1
            yield response.follow(next_page, callback=self.parse)

# divs = response.css('s-item')
# divs = response.css('.s-item__info clearfix')
# fdiv=divs.css('.s-item__info clearfix')
