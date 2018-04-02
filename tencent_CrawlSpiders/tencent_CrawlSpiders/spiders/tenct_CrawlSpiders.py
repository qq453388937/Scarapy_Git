# -*- coding: utf-8 -*-
import scrapy
# 导入链接匹配规则类,用来提取符合规则的链接
from scrapy.linkextractors import LinkExtractor
# 导入CrawlSpider 和Rule
from scrapy.spiders import CrawlSpider,Rule # 之前用的是Spider

class TenctCrawlspidersSpider(CrawlSpider):
    name = 'tenct_CrawlSpiders'
    allowed_domains = ['tencent.com'] # # 可以不写
    start_urls = ['http://tencent.com/']

    rules = (
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        """切记不能和parse重名"""
        i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return i
