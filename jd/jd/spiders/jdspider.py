# -*- coding: utf-8 -*-
import scrapy


class JdspiderSpider(scrapy.Spider):
    name = 'jdspider'
    allowed_domains = ['book.jd.com']
    start_urls = ['https://book.jd.com/booksort.html']

    def parse(self, response):
        pass
