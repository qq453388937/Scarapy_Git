# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule, Spider
from dongguanSpider.items import DongguanspiderItem


class DongguanSpider(Spider):
    """
     # 放到请求队列里,出队,交给下载器去下载,响应提取链接通过LinkExtractor

    """
    """
        from scrapy.linkextractors import LinkExtractor
        link_list=LinkExtractor(allow=("start=\d+"))
        link_list.extract_links(response) # 测试使用
    """
    name = 'xixi'
    allowed_domains = ['wz.sun0769.com']
    page = 0
    base_url = "http://wz.sun0769.com/index.php/question/questionType?type=4&page="

    start_urls = [base_url + str(page)]  # 类属性之间的访问不需要指明,默认就是自己的

    def print_dafa(self, response):
        print(">" * 30 + response.url + "<" * 30)  # 开启日志功能以后,打印和scrapy分离了

    def parse(self, response):
        """从start_urls获取过来的response"""
        self.print_dafa(response)
        # xpath 匹配每一页的所有帖子链接a标签的href属性
        url_list = response.xpath('//div[@class="greyframe"]/table//td/a[@class="news14"]/@href').extract()

        for url in url_list:
            yield scrapy.Request(url, callback=self.parse_item)  # 提取url发起请求下一步处理调用回调函数

        # 翻页,发送下一页的请求回调自己
        self.page += 30
        if self.page <= 1000:
            # 交给请求队列继续请求
            yield scrapy.Request(self.base_url + str(self.page), callback=self.parse)  # 这里是写self.parse 而不是字符串

    def parse_item(self, response):
        """如果出问题如何调试呢?
        注释第二个Rule 只打印第一个Rule的Response.url 并且开启日志
        """
        model = DongguanspiderItem()
        model["title"] = response.xpath("//div[contains(@class,'pagecenter p3')]//strong/text()").extract()[0]
        model["number"] = model["title"].split(" ")[-1].split(":")[-1].strip()

        content = response.xpath("//div[@class='contentext']/text()").extract()
        if len(content) == 0:
            model["content"] = "".join(response.xpath("//div[@class='c1 text14_2']").extract()[0]).strip().replace(
                "\xa0", "")
        else:
            model["content"] = "".join(response.xpath("//div[@class='contentext']/text()").extract()).replace("\xa0",
                                                                                                              "")
        model["url"] = response.url  # 浏览器地址栏中的url,也就是响应体中请求的url
        # 交给管道
        yield model
