# coding = utf-8
from scrapy_redis.spiders import RedisSpider
import re
from liepin.items import LiepinItem
from scrapy import Request


class liepinspider(RedisSpider):
    name = 'liepin'
    redis_key = 'liepin:start_urls'

    def parse(self, response):
        body = response.body.replace('\n', '').replace('\t', '').replace('\r', '')
        info = re.findall(
            '<div class="job-info"><h3 title="(.*?)"><a href="(.*?)" data-promid="(.*?)" target="_blank"onclick="(.*?)">(.*?) </a></h3><p class="condition clearfix"title="(.*?)"><span class="text-warning">(.*?)</span><a href="(.*?)"data-selector="data-url" class="area">(.*?)</a><span class="edu">(.*?)</span><span>(.*?)</span></p><p class="time-info clearfix"><time title="(.*?)">(.*?)</time><span title="(.*?)">(.*?)</span></p></div>',
            body)
        for item in info:
            items = LiepinItem()
            items['title'] = item[0]
            items['info_url'] = item[1]
            items['workinfo'] = item[4]
            items['pay'] = item[6]
            items['worktime'] = item[10]
            yield Request(url=items['info_url'], callback=self.detail, meta={'item': items})

    def detail(self, response):
        item = response.meta['item']
        body = response.body.replace('\n', '').replace('\t', '').replace('\r', '')
        content = re.findall('<div class="content content-word">(.*?)</div>',body)[0].replace('<br/>','')
        companyname = re.findall('class="company-name">(.*?)</a>',body)[0]
        item['content'] = content
        item['companyname'] = companyname
        yield item