# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import json
import pymongo

class DoubanspiderPipeline(object):
    def __init__(self):
        self.file2 = codecs.open("douban.json", "w", encoding="utf-8")  # 比open强大一点的就是编码
        self.file1 = open("douban.json", "w")

    def process_item(self, item, spider):
        json_str = json.dumps(dict(item), ensure_ascii=False)
        self.file2.write(json_str + ",\n")
        return item

    def close_spider(self, spider):
        self.file2.close()
