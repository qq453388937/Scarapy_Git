# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 职位名称
    name = scrapy.Field()
    # 详情链接
    detail_url = scrapy.Field()
    # 职位类别
    category = scrapy.Field()
    # 招牌人数
    number = scrapy.Field()
    # 工作地点
    address = scrapy.Field()
    # publishTime
    pub_date = scrapy.Field()
    # detail_url
    detail_url = scrapy.Field()

class TencentItemPlus(scrapy.Item):
    # define the fields for your item here like:
    # 定义爬取的数据存储的字段
    # 职位名称、详情链接、职位类别、人数、地点、发布时间、岗位职责、岗位要求
    # 职位名称
    name = scrapy.Field()
    # 详情链接
    detail_url = scrapy.Field()
    # 职位类别
    category = scrapy.Field()
    # 招牌人数
    number = scrapy.Field()
    # 工作地点
    address = scrapy.Field()
    # 发布时间
    pub_date = scrapy.Field()
    # 岗位职责
    duty = scrapy.Field()
    # 必须
    require = scrapy.Field()
    pass

