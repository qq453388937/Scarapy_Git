# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs
import pymongo
# scrapy中导入settings文件
from scrapy.conf import settings


class DongguanspiderPipeline(object):
    def __init__(self):
        self.file2 = codecs.open("dongguan2.json", "w", encoding="utf-8")  # 比open强大一点的就是编码
        self.file = open("dongguan.json", "w")

    def open_spider(self, item):
        MONGODB_HOST = settings["MONGODB_HOST"]
        MONGODB_DBNAME = settings["MONGODB_DBNAME"]
        MONGODB_PORT = settings["MONGODB_PORT"]
        MONGODB_TABLE = settings["MONGODB_TABLE"]
        client = pymongo.MongoClient(host=MONGODB_HOST, port=MONGODB_PORT)
        mydb = client[MONGODB_DBNAME] # 选择数据库返回数据库对象
        self.col = mydb[MONGODB_TABLE] # 选择集合返回ｃｏｌｌｅｃｉｔｏｎ对象

    def process_item(self, item, spider):
        json_str = json.dumps(dict(item), ensure_ascii=False)
        self.file.write(json_str + ",\n")
        self.col.insert(dict(item))
        return item

    def close_spider(self, spider):
        self.file.close()
