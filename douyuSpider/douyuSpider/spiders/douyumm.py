# -*- coding: utf-8 -*-
import scrapy, json, time

from douyuSpider.items import DouyuspiderItem


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
            yield scrapy.Request(self.url + str(self.offset), callback=self.parse,dont_filter=True)
        pxd = 1

        import  re
