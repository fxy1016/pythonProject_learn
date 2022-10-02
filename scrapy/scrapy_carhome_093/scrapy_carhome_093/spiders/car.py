import scrapy


class CarSpider(scrapy.Spider):
    name = 'car'
    allowed_domains = ['https://car.autohome.com.cn/price/brand-14.html']
    start_urls = ['https://car.autohome.com.cn/price/brand-14.html']

    def parse(self, response):
        name_list = response.xpath('//div[@class="main-title"]/a/text()')
        for name in name_list:
            print(name.extract())
