from scrapy_redis.spiders import RedisSpider


class MySpider(RedisSpider):
    """
    Spider that reads urls from redis queue (myspider:start_urls).
    分布式爬虫
    """
    name = 'myspider_redis'
    # 起来所有端爬虫的命令1
    # 没有start_urls 通过lpush来启动
    redis_key = 'myspider:start_urls'

    # __init__ 等效于 allowed_domains=["xxxx.com"] # 下面是动态获取域的范围
    def __init__(self, *args, **kwargs):
        """allowed_domains 替换成了 官方提供的动态获取爬取请求域的范围换成了 可选项目"""
        # Dynamically define the allowed domains list.
        domain = kwargs.pop('domain', '')
        self.allowed_domains = filter(None, domain.split(','))
        # 复制黏贴改一下super的第一个参数是当前的类名(MySpider)就可以了
        super(MySpider, self).__init__(*args, **kwargs)

    def parse(self, response):
        return {
            'name': response.css('title::text').extract_first(),
            'url': response.url,
        }
"""
cd spiders/ 里面来
scrapy runspider myspider_redis.py 即可
lpush myspider:start_url "网站"
任务完成之后再次进入等待状态
"""