# -*- coding:utf-8 -*-
import scrapy
from mySpider.items import TeacherItem


class teacherSpider(scrapy.Spider):
    name = "fb"
    # 允许爬虫作用的范围
    allowd_domains = ["http://www.itcast.cn/"]
    # 元祖列表都可以
    start_urls = [
        "http://www.itcast.cn/channel/teacher.shtml#apython",
    ]

    def parse(self, response):  # 并发异步都不用关心
        # with open("teacher.html", "w") as f:
        #     f.write(response.body)
        # 通过resonse.xpath 匹配出老师的根节点
        # 所有老师的集合
        tmp_arr = []
        for item in response.xpath("//div[@class='li_txt']"):
            teacher = TeacherItem()
            # 遍历   不加extract就是xpath匹配度西
            name = item.xpath("./h3/text()").extract()  # 只要是XPATH匹配的都是列表['']  先用extract() 将匹配出来的转换为unicode字符串
            title = item.xpath("./h4/text()").extract()  # 只要是XPATH匹配的都是列表[''] 先用extract()将匹配出来的转换为unicode字符串
            info = item.xpath("./p/text()").extract()  # 只要是XPATH匹配的都是列表[''] 先用extract()将匹配出来的转换为unicode字符串
            # print(name[0])
            # print(zhi_cheng[0])
            # print(info[0])
            teacher["name"] = name[0]
            teacher["title"] = title[0]
            teacher["info"] = info[0] # 

            tmp_arr.append(teacher)
        # 返回数据，不经过pipeline
        return tmp_arr  #

# class A(object):
#     def __init__(self):
#         self.name = 'xiaomin'
#
# def fun():
#     for i in range(100):
#         time.sleep(10)
#         print i
#         if i == 70:
#             print bbbb
#
#
# print A().age
