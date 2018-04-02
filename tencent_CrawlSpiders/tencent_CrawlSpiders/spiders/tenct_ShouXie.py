# -*- coding:utf-8 -*-

import scrapy
# 导入链接匹配规则类,用来提取符合规则的链接
from scrapy.linkextractors import LinkExtractor
# 导入CrawlSpider 和Rule
from scrapy.spiders import CrawlSpider, Rule  # 之前用的是Spider
from tencent_CrawlSpiders.items import TencentItem


class TenctCrawlspidersSpider_Shouxie(CrawlSpider):
    name = "tc_shouxie"
    allowed_domains = ['tencent.com']  # 可以不写
    start_urls = ['https://hr.tencent.com/position.php?&start=0#a']
    # response里的链接提取
    page_link = LinkExtractor(allow=("start=\d+",))
    # new_link = LinkExtractor(allow=("positon.php",))

    rules = [
        # 符合规则的深度请求,获取这个列表里的链接依次发送请求,并且继续跟进调用指定的回调函数  parseTencent 继续处理
        Rule(page_link, callback="parseTencent", follow=True),
        # Rule(new_link,callback="parseTencent",follow=True)
    ]

    #
    def parseTencent(self, response):
        """切记不能和parse重名"""
        # response.xpath("//tr[@class='even']")+response.xpath("//tr[@class='odd']") xpath 本质就是一个列表,可以相加合并"或"的条件到一个列表中
        for item in response.xpath("//tr[@class='even']|//tr[@class='odd']"):
            tencent_model = TencentItem()  # 当做假字典来用
            # 职位名称
            tencent_model["positionname"] = item.xpath("./td[1]/a/text()").extract()[0]
            # 详情链接
            tencent_model["positionlink"] = item.xpath("./td[1]/a/@href").extract()[0]
            # 职位类别
            tencent_model["positionType"] = item.xpath("./td[2]/text()").extract()[0] if item.xpath(
                "./td[2]/text()") else ""
            # 招牌人数
            tencent_model["peopleNum"] = item.xpath("./td[3]/text()").extract()[0]
            # 工作地点
            tencent_model["worklocation"] = item.xpath("./td[4]/text()").extract()[0]
            # publishTime
            tencent_model["publishtime"] = item.xpath("./td[5]/text()").extract()[0]
            yield item
        # 下一页请求不需要自己去发了,由scrapy帮我们发送,深度请求
