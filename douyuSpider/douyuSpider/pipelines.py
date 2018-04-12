# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
# settings  获取scrapy的设置文件
from scrapy.utils.project import get_project_settings
# 导入piplines中的images处理的方法类
from scrapy.pipelines.images import ImagesPipeline
import os, json


class DouyuImagePipeline(ImagesPipeline):
    number = 0
    # 获取scrapy中settings中的设置的IMAGES_STORE的值
    IMAGES_STORE = get_project_settings().get("IMAGES_STORE")

    # 重写方法,
    def get_media_requests(self, item, info):
        """获取图片的链接并且发送请求"""
        image_url = item["vertical_src"]
        yield scrapy.Request(image_url)  # 这里不需要回调

    def item_completed(self, result, item, info):
        """
        图片请求完毕后处理的请求
        result 是什么？？？？？

        <class 'tuple'>: (True, {'url': 'https://rpic.douyucdn.cn/live-cover/appCovers/2018/03/01/3559600_20180301211036_big.jpg', 'checksum': 'cdb42ca421a9c2c89dcead50fa273d8c', 'path': 'full/b105870254d4e82f65ede7add3d05f022958ddb4.jpg'})
        """
        print("+++"*20)
        print(result)
        self.number += 1
        image_path = [x["path"] for ok, x in result if ok]

        os.rename(self.IMAGES_STORE + image_path[0],#image_path[0] ==> full/b105870254d4e82f65ede7add3d05f022958ddb4.jpg
                  self.IMAGES_STORE + str(self.number) + "_" + item["nickname"] + ".jpg")
        # 存储到对象的属性中
        item["vertical_src"] = self.IMAGES_STORE + "/" + item["nickname"]

        return item

    def close_spider(self, spider):
        os.rmdir(self.IMAGES_STORE + "/full")


# 存储文件并且存储一份数据到ｊｓｏｎ
class DouyuStoragePipeline(object):
    def __init__(self):
        """可选的方法,初始化方法"""
        self.file = open("douyu.json", "w")  # 这里为什么不能写encoding?

        #  item 就是传过来的TeacherItem 对象

    def process_item(self, item, spider):  # spider是爬虫名字
        """管道文件处理数据,处理item数据的"""
        json_str = json.dumps(dict(item), ensure_ascii=False)
        self.file.write(json_str + ",\n")
        return item  # 不管写什么最后要return

    def close_spider(self, spider):
        """可选方法,类似析构方法"""
        self.file.close()
