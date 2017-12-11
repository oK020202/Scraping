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
    post_id = scrapy.Field()
    post_author = scrapy.Field()
    post_name = scrapy.Field()
    post_title = scrapy.Field()
    post_content = scrapy.Field()
    post_date = scrapy.Field()
    post_category = scrapy.Field()
    post_type = scrapy.Field()
    post_status = scrapy.Field()
    post_tags = scrapy.Field()
    custom_field = scrapy.Field()
    
    image_urls = scrapy.Field()
    images = scrapy.Field()