# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class C4JtumblrItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class NewsItem(scrapy.Item):
    article_id = scrapy.Field()
    title = scrapy.Field()
    body = scrapy.Field()
    time = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()