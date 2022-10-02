import scrapy


class TcSpider(scrapy.Spider):
    name = 'tc'
    allowed_domains = ['https://xm.58.com']
    start_urls = ['https://xm.58.com/']

    def parse(self, response):
        print('和三栋菏泽曹县')
