# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DzItem(scrapy.Item):
    source_id = scrapy.Field()
    author = scrapy.Field()
    content = scrapy.Field()
    post_date = scrapy.Field()
    like_count = scrapy.Field()
    comment_count = scrapy.Field()
        
