# -*- coding: utf-8 -*-
import scrapy


class BaiduSpider(scrapy.Spider):
    name = 'jingdong'
    allowed_domains = ['jingdong.com']
    # start_urls = ['http://baidu.com/']
    start_urls = ["https://book.suning.com/"]
    custom_settings = {
        "DEFAULT_REQUEST_HEADERS": {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
                          " (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
        }
    }

    def parse(self, response):
        print(response.text)
