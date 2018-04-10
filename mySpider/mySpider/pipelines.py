# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json


class PeiXiaoDongPipeline(object):
    def __init__(self):
        """可选的方法,初始化方法"""
        self.file = open("teacher.json", "w")  # 这里为什么不能写encoding?

    #  item 就是传过来的TeacherItem 对象
    def process_item(self, item, spider):  # spider是爬虫名字
        """管道文件处理数据,处理item数据的"""
        json_str = json.dumps(dict(item), ensure_ascii=False)
        self.file.write(json_str.encode("utf-8") + ",\n")
        return item  # 不管写什么最后要return

    def close_spider(self, spider):
        """可选方法,类似析构方法"""
        self.file.close()
