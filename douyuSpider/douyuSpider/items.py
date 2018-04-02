# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DouyuspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 主播名称
    nickname = scrapy.Field()
    # 图片的远程链接
    vertical_src = scrapy.Field()
    # 图片的本地路径
    image_path = scrapy.Field()
    pass
