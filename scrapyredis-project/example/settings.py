# Scrapy settings for example project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#
SPIDER_MODULES = ['example.spiders']
NEWSPIDER_MODULE = 'example.spiders'

USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3'

# scrapy-redis去重组件必备配置文件1 去重组件 (和原来scrapy的配置不冲突可以共存)
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"  # 不适用默认的去重,scrapy的去重
# scrapy-redis调度器组件必备配置文件2 调度器组件 (和原来scrapy的配置不冲突可以共存)
SCHEDULER = "scrapy_redis.scheduler.Scheduler"  # 不适用scrapy默认的调度器,重写了
# scrapy-redis调度器保持组件必备配置文件3 断点续爬
SCHEDULER_PERSIST = True  # 可以暂停,断点续爬 (和原来scrapy的配置不冲突可以共存)
# 默认的scrapy请求集合 一般不开启, 按sorted排序
# SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderPriorityQueue"
# 先进先出 # scrapy-redis组件必备可选配置文件3.5 请求队列存储到redis里面
SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderQueue"
# 先进后出
# SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderStack"
# scrapy_redis 管道
ITEM_PIPELINES = {
    'example.pipelines.ExamplePipeline': 300,
    # scrapy-redis组件必备配置文件4 管道文件存储数据到redis (和原来scrapy的配置不冲突可以共存)
    'scrapy_redis.pipelines.RedisPipeline': 400,  # 数据存储到redis必须带,scrapy_redis必须启动
}
# redis设置 键是固定写法  scrapy-redis组件必备配置文件5  (和原来scrapy的配置不冲突可以共存)

# REDIS_HOST = "127.0.0.1" # 可以设置远程IP
# REDIS_PORT = "6379"
REDIS_URL = "redis://127.0.0.1:6379"
# LOG_LEVEL = 'DEBUG'

# Introduce an artifical delay to make use of parallelism. to speed up the
# crawl.

# 下载延迟
DOWNLOAD_DELAY = 1
