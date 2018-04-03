# -*- coding: utf-8 -*-
import scrapy


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['douban.com']
    start_urls = ['http://douban.com/']
    """
    电影名称: //div[@class='item']//a/span[1]
    电影描述: //div[@class='info']/div[@class='bd']/p[1]
    评分: //span[@class='rating_num']
    口号: //p[@class='quote']
    """
    def parse(self, response):
        pass
