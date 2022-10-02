import scrapy

from ..items import ScrapyMovie099Item


class MvSpider(scrapy.Spider):
    name = 'mv'
    # https://www.ygdy8.net/html/gndy/china/index.html
    allowed_domains = ['ygdy8.net']
    start_urls = ['https://www.ygdy8.net/html/gndy/china/index.html']

    def parse(self, response):
        # 没有反扒
        # print('hhhhhhh')
        a_list = response.xpath('//ul//td/b/a[2]')

        for a in a_list:
            # 爬取第一页的电影名字和要进入的链接
            name = a.xpath('./text()').extract_first()
            href = a.xpath('./@href').extract_first()
            # 拼接第二页的地址
            url = 'https://www.ygdy8.net' + href
            # 对第二页进入

            yield scrapy.Request(url=url, callback=self.parse_second,meta={'name':name})
    def parse_second(self,response):
        # print('你几把谁啊')
        # 图片链接
        # //div[@id="Zoom"]/span/img/@src
        # src = response.xpath('//div[@id="Zoom"]/span/img/@src').extract_first()
        src = response.xpath('//div[@id="Zoom"]//img/@src').extract_first()
        # 获取的为none，因为span识别不了
        # 接收参数
        name = response.meta['name']
        movie = ScrapyMovie099Item(name=name, src=src)
        yield movie

