# -*- coding:utf-8 -*-

import scrapy
# 导入链接匹配规则类,用来提取符合规则的链接 有s的地方导入没有s的
from scrapy.linkextractors import LinkExtractor
# 导入CrawlSpider 和Rule
from scrapy.spiders import CrawlSpider, Rule  # 之前用的是Spider
from tencent_CrawlSpiders.items import TencentItem

"""
Link Extractors 的目的很简单: 提取链接｡

每个LinkExtractor有唯一的公共方法是 extract_links()，它接收一个 Response 对象，并返回一个 scrapy.link.Link 对象。

Link Extractors要实例化一次，并且 extract_links 方法会根据不同的 response 调用多次提取链接｡

scrapy shell "http://wz.sun0769.com/html/question/201804/365467.shtml"
print response.xpath("//div[@class='pagecenter p3']//strong/text()").extract()[0].split(" ")[-1].split(":")[-1]

"""


class TenctCrawlspidersSpider_Shouxie(CrawlSpider):
    """
    from scrapy.linkextractors import LinkExtractor
    link_list=LinkExtractor(allow=("start=\d+"))
    link_list.extract_links(response) # 测试使用
    """
    name = "tc"
    allowed_domains = ['hr.tencent.com']  # 可以不写
    start_urls = ['https://hr.tencent.com/position.php?&start=0#a'] # 第一次请求start_urls
    # response里的链接提取链接url,搭配rules使用, 返回符合匹配规则链接的列表
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
        if response.xpath("//tr[@class='even']|//tr[@class='odd']"):
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
                tencent_model["peopleNum"] = item.xpath("./td[3]/text()").extract()[0] if item.xpath(
                    "./td[3]/text()") else ""
                # 工作地点
                tencent_model["worklocation"] = item.xpath("./td[4]/text()").extract()[0] if item.xpath(
                    "./td[4]/text()") else ""
                # publishTime
                tencent_model["publishtime"] = item.xpath("./td[5]/text()").extract()[0] if item.xpath(
                    "./td[5]/text()") else ""
                yield tencent_model  # 一定要return假字典
        # 下一页请求不需要自己去发了,由scrapy帮我们发送,深度请求
