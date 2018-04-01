# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TeacherItem(scrapy.Item):
    # 姓名
    name = scrapy.Field() # 实际上就是字符串
    # 职称
    title = scrapy.Field() # 实际上就是字符串
    # 个人简介
    info = scrapy.Field() # 实际上就是字符串
