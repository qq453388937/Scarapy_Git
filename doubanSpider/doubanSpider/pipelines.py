# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import json
import pymongo
# 导入settings文件
from scrapy.conf import settings


class DoubanspiderPipeline(object):
    def __init__(self):
        self.file2 = codecs.open("douban.json", "w", encoding="utf-8")  # 比open强大一点的就是编码
        self.file1 = open("douban.json", "w")
        MONGODB_HOST = settings["MONGODB_HOST"]
        MONGODB_DBNAME = settings["MONGODB_DBNAME"]
        MONGODB_PORT = settings["MONGODB_PORT"]
        MONGODB_TABLE = settings["MONGODB_TABLE"]
        client = pymongo.MongoClient(host=MONGODB_HOST, port=MONGODB_PORT)
        mydb = client[MONGODB_DBNAME]
        self.post = mydb[MONGODB_TABLE]

    def open_spider(self,item):
        pass # 类比与__init__方法

    def process_item(self, item, spider):
        json_str = json.dumps(dict(item), ensure_ascii=False)
        # 存储数据库
        self.post.insert(json.loads(json_str))
        self.file2.write(json_str + ",\n")


        return item

    def close_spider(self, spider):
        self.file2.close()
        self.file1.close()
