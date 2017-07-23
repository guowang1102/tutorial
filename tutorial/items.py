# -*- coding: utf-8 -*-
# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
import scrapy

# class TutorialItem(scrapy.Item):
#     # define the fields for your item here like:
#     # name = scrapy.Field()
#    pass

class Aqu1024Item(scrapy.Item):
    title = scrapy.Field()  # 标题
    url = scrapy.Field()    # URL
    author = scrapy.Field()   # 作者
    lastUpdateTime = scrapy.Field()  # 最后更新时间
    

