# -*- coding: utf-8 -*-
import scrapy, json, time

from douyuSpider.items import DouyuspiderItem
from scrapy.linkextractors import LinkExtractor
from scrapy.linkextractors import LinkExtractor
#
# link_list = LinkExtractor(allow=("start=\d+")) # 返回的就是Ruler对象
# link_list.extract_links(response) # 每个LinkExtractor有唯一的公共方法是 extract_links()，它接收一个 Response 对象，并返回一个 scrapy.link.Link 对象。
"""
[Link(url='https://hr.tencent.com/position.php?&start=10#a', text='2', fragment='', nofollow=False), Link(url='https://hr.tencent.com/position.php?&start=20#a', text='3', fragment='', nofollow=False), Link(url='https://hr.tencent.com/position.php?&start=30#a', text='4', fragment='', nofollow=False), Link(url='https://hr.tencent.com/position.php?&start=40#a', text='5', fragment='', nofollow=False), Link(url='https://hr.tencent.com/position.php?&start=50#a', text='6', fragment='', nofollow=False), Link(url='https://hr.tencent.com/position.php?&start=60#a', text='7', fragment='', nofollow=False), Link(url='https://hr.tencent.com/position.php?&start=70#a', text='...', fragment='', nofollow=False), Link(url='https://hr.tencent.com/position.php?&start=3920#a', text='393', fragment='', nofollow=False)]


class scrapy.spiders.Rule(
        link_extractor, 
        callback = None, # 当编写爬虫规则时，避免使用parse作为回调函数。由于CrawlSpider使用parse方法来实现其逻辑，如果覆盖了 parse方法，crawl spider将会运行失败。 
        cb_kwargs = None, 
        follow = None, 
        process_links = None, 
        process_request = None
)
"""


class DouyummSpider(scrapy.Spider):
    name = 'douyumm'
    allowed_domains = ['capi.douyucdn.cn']
    url = "http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset="
    offset = 0
    # 只会获取一次从迭代器
    start_urls = [url + str(offset)]

    def parse(self, response):
        """解析方法"""
        json_str = response.body.decode()
        my_dict = json.loads(json_str).get("data")
        if my_dict:
            for item in my_dict:
                douyumm = DouyuspiderItem()
                douyumm["nickname"] = item["nickname"]
                douyumm["vertical_src"] = item["vertical_src"]
                yield douyumm
                # 如果写到for 循环里面 yield的本质是放入队列等待下载
                # yield scrapy.Request(self.url + str(self.offset), callback=self.parse, dont_filter=True)
            self.offset += 20
            # dont_filter 忽略域组,解决加上allowed_domains http://的问题
            yield scrapy.Request(self.url + str(self.offset), callback=self.parse, dont_filter=True)
        pxd = 1

        import re
