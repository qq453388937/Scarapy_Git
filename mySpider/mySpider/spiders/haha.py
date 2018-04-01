# -*- coding: utf-8 -*-
import scrapy


class HahaSpider(scrapy.Spider):
    name = "haha"
    allowed_domains = ["itcast.cn"]
    start_urls = (
        'http://www.itcast.cn/',
    )

    def parse(self, response):
        pass
