# -*- coding: utf-8 -*-
import scrapy


# 只要是需要提供post数据的，就可以用这种方法，
# 下面示例：post数据是账户密码
class Renren1Spider(scrapy.Spider):
    name = "renren1"
    allowed_domains = ["renren.com"]

    # 实现post请求，重写start_requests方法，因为Spider类中默认实现的Request请求，请求方法为GET
    def start_requests(self):
        """建议使用这种"""
        url = 'http://www.renren.com/PLogin.do'
        yield scrapy.FormRequest(
            url=url,
            formdata={"email": "mr_mao_hacker@163.com", "password": "alarmchime"}, # ｎａｍｅ属性email和password
            callback=self.parse_page)

    def parse_page(self, response):
        with open("mao2.html", "w") as filename:
            filename.write(response.body)
