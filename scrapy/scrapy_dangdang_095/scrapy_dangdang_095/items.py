# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyDangdang095Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pic
    src = scrapy.Field()
    # name of book
    name = scrapy.Field()
    # price of book
    price = scrapy.Field()

