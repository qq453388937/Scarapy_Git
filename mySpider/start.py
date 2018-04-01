# -*- coding:utf-8 -*-
import sys

from scrapy import cmdline

cmdline.execute("scrapy crawl fb -o ../fb.json".split()) # 默认是当前路径
