# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json


class TencentCrawlspidersPipeline(object):
    def __init__(self):
        self.file = open("tencent_Crawlspider.json", "w")

    def process_item(self, item, spider):
        json_str = json.dumps(dict(item), ensure_ascii=False)
        self.file.write(json_str + ",\n")
        return item

    def close_spider(self, spider):
       self.file.close()