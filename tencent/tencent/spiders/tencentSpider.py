# -*- coding:utf-8 -*-

import scrapy

from tencent.items import TencentItem


# 将数据交给管道处理

# 将请求重新发送给调度器队列.出队列,交给下载器下载

class TencentSpider(scrapy.Spider):
    # 爬虫的名称,很关键,启动命令用到
    name = "tencent"
    # 允许爬虫作用的范围
    allowed_domains = ["tencent.com"]
    url = "http://hr.tencent.com/position.php?&start="
    page = 0
    # 元祖列表都可以
    start_urls = [url + str(page)]

    def parse(self, response):
        print(response.body)
        for item in response.xpath("//tr[@class='even']|//tr[@class='odd']"):
            # response.xpath("//tr[@class='even']|//tr[@class='odd']")[0].xpath("td[1]/a/text()").extract()[0] 测试
            tencent_model = TencentItem()  # 当做假字典来用
            # 职位名称
            tencent_model["positionname"] = item.xpath("./td[1]/a/text()").extract()[0]
            # 详情链接
            tencent_model["positionlink"] = item.xpath("./td[1]/a/@href").extract()[0]
            # 职位类别
            tencent_model["positionType"] = item.xpath("./td[2]/text()").extract()[0]
            # 招牌人数
            tencent_model["peopleNum"] = item.xpath("./td[3]/text()").extract()[0]
            # 工作地点
            tencent_model["worklocation"] = item.xpath("./td[4]/text()").extract()[0]
            # publishTime
            tencent_model["publishtime"] = item.xpath("./td[5]/text()").extract()[0]

            # 将数据交给管道文件处理 pipelines
            yield tencent_model
        # 个人理解为类属性可以通过对象的方法点出来
        if self.page < 1680:
            # 自增10每次处理完一页请求后处理下一页请求
            self.page += 10
        # 下一页请求 回调自己
        yield scrapy.Request(self.url + str(self.page), callback=self.parse)
