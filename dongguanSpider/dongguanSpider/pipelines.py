# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs
# scrapy中导入settings文件
from scrapy.conf import settings


class DongguanspiderPipeline(object):
    def __init__(self):
        self.file2 = codecs.open("dongguan2.json", "w", encoding="utf-8")  # 比open强大一点的就是编码
        self.file = open("dongguan.json", "w")

    def process_item(self, item, spider):
        json_str = json.dumps(dict(item), ensure_ascii=False)
        self.file.write(json_str + ",\n")
        return item

    def close_spider(self, spider):
        self.file.close()
