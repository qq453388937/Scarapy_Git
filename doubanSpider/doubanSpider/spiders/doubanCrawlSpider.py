# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from doubanSpider.items import DoubanspiderItem


class DoubanCrawlSpider(CrawlSpider):
    name = 'db'
    allowed_domains = ['movie.douban.com']
    page = 0
    base_url = 'https://movie.douban.com/top250?start='
    start_urls = [base_url + str(page)]

    rules = [
        Rule(LinkExtractor(allow=(r"start=\d+&filter=",)), follow=True,callback="parse_Douban")
    ]
    """
    电影名称: //div[@class='item']//a/span[1]
    电影描述: //div[@class='info']/div[@class='bd']/p[1]
    评分: //span[@class='rating_num']
    口号: //p[@class='quote']
    """

    def parse_Douban(self, response):
        # return
        print(response.url)
        for i in range(0, 25): # 可以获取父类的ｘｐａｔｈ（２５个）遍历当前ｘｐａｔｈ节点也可以直接取子节点
            item = DoubanspiderItem()
            item["title"] = response.xpath("//div[@class='item']//a/span[1]/text()").extract()[i]
            item["bd"] = response.xpath("//div[@class='info']/div[@class='bd']/p[1]/text()").extract()[i]
            item["star"] = response.xpath("//span[@class='rating_num']/text()").extract()[i]
            item["quote"] = response.xpath("//p[@class='quote']").extract()[i]
            yield item
        # self.page += 10
        # url = self.base_url + str(self.page)
        # yield scrapy.Request(url, callback=self.parse)
