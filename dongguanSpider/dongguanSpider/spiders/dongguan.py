# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from dongguanSpider.items import DongguanspiderItem


class DongguanSpider(CrawlSpider):
    """
     # 放到请求队列里,出队,交给下载器去下载,响应提取链接通过LinkExtractor

    """
    """
        from scrapy.linkextractors import LinkExtractor
        link_list=LinkExtractor(allow=("start=\d+"))
        link_list.extract_links(response) # 测试使用
    """
    name = 'dongguan'
    allowed_domains = ['wz.sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4&page=0']

    # page_link = LinkExtractor(allow=r"questionType?type=4&page=0")
    rules = [
        # 没有callback 意味着 follow = True
        Rule(LinkExtractor(allow=r'type=4&page=\d+'), follow=True, callback="print_dafa", process_links="deal_links"),
        # 这个页面不需要抓取数据就不用写ｃａｌｌｂａｃｋ
        # 进去详情页就不需要深度爬取了所以follow=False
        Rule(LinkExtractor(allow=r"/html/question/\d+/\d+.shtml"), follow=False, callback="parse_item")
    ]

    def print_dafa(self, response):
        print(">" * 30 + response.url + "<" * 30)  # 开启日志功能以后,打印和scrapy分离了

    def parse_item(self, response):
        """如果出问题如何调试呢?
        注释第二个Rule 只打印第一个Rule的Response.url 并且开启日志
        """
        model = DongguanspiderItem()
        model["title"] = response.xpath("//div[contains(@class,'pagecenter p3')]//strong/text()").extract()[0]
        model["number"] = model["title"].split(" ")[-1].split(":")[-1].strip()

        content = response.xpath("//div[@class='contentext']/text()").extract()
        if content:
            model["content"] = "".join(response.xpath("//div[@class='c1 text14_2']").extract()[0]).strip().replace(
                "\xa0", "")
        else:
            model["content"] = "".join(response.xpath("//div[@class='contentext']/text()").extract()).replace("\xa0",
                                                                                                              "")
        model["url"] = response.url  # 浏览器地址栏中的url,也就是响应体中请求的url
        yield model

    def deal_links(self, links):
        """
        links 就是从LinkExtrator中匹配出来的列表
        Type&page=xxx?type=4修改为Type?page=xxx&type=4
        """
        for link in links:
            link.url = link.url.replace("?", "&").replace("Type&", "Type?")
            print(link.url)  # url 属性能获取出url
        return links  # 修改完毕要返回否则只会执行一次!!!!!
