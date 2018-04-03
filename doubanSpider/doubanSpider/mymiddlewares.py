# -*- coding:utf-8 -*-
# 导入settings文件
# from scrapy.conf import settings

from .settings import USER_AGENTS
from .settings import PROXIES
import base64
import random


class RandomUserAgent(object):
    def process_request(self, request, spider):
        user_agent = random.choice(USER_AGENTS)
        request.headers.setdefault("User-Agent", user_agent)


class RandomProxy(object):
    def process_request(self, request, spider):
        proxy = random.choice(PROXIES)
        if proxy["user_password"] is None:
            # 没有代理账户验证的话
            request.meta["proxy"] = "http://" + proxy["ip_port"]
        else:
            b64_user_passwd = base64.b64encode(proxy["user_passwd"])
            # ip代理固定写法
            request.meta["proxy"] = "http://" + proxy["ip_port"]
            request.headers["Proxy-Authorization"] = "Basic " + b64_user_passwd
