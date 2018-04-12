# -*- coding:utf-8 -*-

import scrapy

from tencent.items import TencentItem,TencentItemPlus


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
        # print(response.body)
        for item in response.xpath("//tr[@class='even']|//tr[@class='odd']"):
            # response.xpath("//tr[@class='even']|//tr[@class='odd']")[0].xpath("td[1]/a/text()").extract()[0] 测试
            tencent_model = TencentItemPlus()  # TencentItem()  # 当做假字典来用
            # 职位名称
            tencent_model["name"] = item.xpath("./td[1]/a/text()").extract()[0]
            # 详情链接
            tencent_model["detail_url"] = item.xpath("./td[1]/a/@href").extract()[0]
            # 职位类别
            tencent_model["category"] = item.xpath("./td[2]/text()").extract()[0] if item.xpath(
                "./td[2]/text()") else ""
            # 招牌人数
            tencent_model["number"] = item.xpath("./td[3]/text()").extract()[0]
            # 工作地点
            tencent_model["address"] = item.xpath("./td[4]/text()").extract()[0]
            # publishTime
            tencent_model["pub_date"] = item.xpath("./td[5]/text()").extract()[0]
            # detail_url
            tencent_model["detail_url"] = 'https://hr.tencent.com/' + item.xpath('./td[1]/a/@href').extract()[0]
            # extract_first()默认提取第一条，如果未提取到，给默认值，不会报异常

            # 将数据交给管道文件处理 pipelines
            # yield tencent_model
            yield scrapy.Request(
                tencent_model["detail_url"],
                callback=self.parse_detail,
                meta={'meta1': tencent_model}
            )

        # 个人理解为类属性可以通过对象的方法点出来
        if self.page < 1680:
            # 自增10每次处理完一页请求后处理下一页请求
            self.page += 10
        # 下一页请求 回调自己self.parse 处理response
        yield scrapy.Request(self.url + str(self.page), callback=self.parse)

    def parse_detail(self, response):
        # 获取传递过来的ｉｔｅｍ
        item = response.meta["meta1"]
        # 提取详情页的信息
        item['duty'] = response.xpath('//tr[3]/td/ul/li/text()').extract()[0]
        item['require'] = response.xpath('//tr[4]/td/ul/li/text()').extract()[0]
        # 提取完毕强请页面的返回item给引擎
        yield item
