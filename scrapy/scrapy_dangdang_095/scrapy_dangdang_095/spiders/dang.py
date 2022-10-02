import scrapy

# python真是bug频出啊
from ..items import ScrapyDangdang095Item


class DangSpider(scrapy.Spider):
    name = 'dang'
    allowed_domains = ['category.dangdang.com']
    start_urls = ['https://category.dangdang.com/cp01.01.02.00.00.00.html']
    base_url = 'https://category.dangdang.com/pg'
    page = 1

    # https://category.dangdang.com/pg2-cp01.01.02.00.00.00.html
    def parse(self, response):
        # src = ' //ul[@id="component_59"]/li//img/@src'
        # alt = ' //ul[@id="component_59"]/li//img/@alt'
        # price = '//ul[@id="component_59"]/li/p[@class="price"]/span[@class="search_now_price"]/text()
        li_list = response.xpath('//ul[@id="component_59"]/li')
        for li in li_list:
            # 第一张图片可以使用src
            src = li.xpath('.//img/@data-original').extract_first()
            if src:
                src = src
            else:
                src = li.xpath('.//img/@src').extract_first()
            name = li.xpath('.//img/@alt').extract_first()
            price = li.xpath('.//p[@class="price"]/span[@class="search_now_price"]/text()').extract_first()

            book = ScrapyDangdang095Item(src=src, name=name, price=price)
            # 获取一个book就返回yield，交给pipelines
            yield book
        if self.page < 100:
            self.page = self.page + 1
            url = self.base_url + str(self.page) + '-cp01.01.02.00.00.00.html'

            yield scrapy.Request(url=url, callback=self.parse)
