# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LiepinItem(scrapy.Item):
    title = scrapy.Field()
    companyname = scrapy.Field()
    content = scrapy.Field()
    worktime = scrapy.Field()
    workinfo = scrapy.Field()
    pay = scrapy.Field()
    info_url = scrapy.Field()
