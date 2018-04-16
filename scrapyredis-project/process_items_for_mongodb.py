# -*- coding:utf-8 -*-
import redis
import pymongo
import json


def process_items():
    rediscli = redis.Redis(host="127.0.0.1", port=6379, db=0)
    mongocli = pymongo.MongoClient(host="127.0.0.1", port=27017)

    # 创建mongoDB数据库的名称
    db = mongocli["youyuan"]
    col = db["my_collection"]
    offset = 0
    while True:
        source, data = rediscli.blpop("redis_key_list")
        offset += 1
        data = json.loads(data)
        col.insert(data)  # 插入字典
        print(offset)


if __name__ == '__main__':
    process_items()
