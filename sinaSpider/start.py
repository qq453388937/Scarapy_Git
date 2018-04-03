# -*- coding:utf-8 -*-
import sys



from scrapy import cmdline

# dont forget "".split() function

# cmdline.execute("scrapy crawl fb -o ../fb.json".split())  # 默认是当前路径  ../ 是上一级目录


cmdline.execute("scrapy crawl sa".split())


# def fib(num):
#     a, b, sum = 0, 1, 0
#     while sum < num:
#         a, b = b, a + b
#         sum = sum + 1
#         # print(b)
#         yield b


# res = fib(5)
# res.next()
# res.next()
# res.next()
# res.next()

# 也可以通过循环的方式,生成器就是特殊的迭代器,可以遍历
# for item in fib(5):
#     print(item)
