import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = ['https://www.rewardhospitality.com.au/search?ProductSearch=oven']

    def parse(self, response):

        title = response.css('.author::text').extract()
        for item in zip(title):
            print(item)
            product_name = scrapy.Field()
            href=scrapy.Field()

            item['product_name'] = item[0]
    # new_item['href']=item[1]

            yield item
#
# all_title = response.css('.widget-productlist-code::text').extract()
# title = response.xpath("//span[@class='a']/text()").extract()
# for title in all_title:
#     print title
# for x in title:
#     print x
# yield {title}
