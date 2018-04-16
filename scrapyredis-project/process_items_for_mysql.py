# -*- coding:utf-8 -*-
import redis
import pymysql
import json


def process_item():
    redis_cli = redis.Redis(host="127.0.0.1", port=6379, db=0)
    mysql_cli = pymysql.connect(host='localhost', port=3306, user='root', password='123', database='xxx', \
                                charset='utf8')
    cursor = mysql_cli.cursor()
    offset = 0
    while True:
        offset += 1
        source, data = redis_cli.blpop("redis_key")
        dict_data = json.loads(data)
        cursor.execute("insert into xxx values(%s,%s)", dict_data[""], dict_data[""])
        print(offset)
    mysql_cli.commit()
    cursor.close()
    mysql_cli.close()