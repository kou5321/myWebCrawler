# -*- coding: utf-8 -*-
import scrapy


class BeautyspiderSpider(scrapy.Spider):
    name = 'beautySpider'
    allowed_domains = ['https://www.cnblogs.com/passagain/p/11449178.html']
    start_urls = ['http://https://www.cnblogs.com/passagain/p/11449178.html/']

    def parse(self, response):
        pass
