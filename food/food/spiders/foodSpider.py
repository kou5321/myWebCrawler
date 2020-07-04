# -*- coding: utf-8 -*-
import scrapy
from ..items import FoodItem


class FoodspiderSpider(scrapy.Spider):
    name = 'foodSpider'
    allowed_domains = ['https://www.meishij.net/']
    start_urls = ['https://www.meishij.net/china-food/caixi/chuancai/']

    def parse(self, response):
        list1 = []
        src_list = response.xpath('//div[@class="liststyle1_w clearfix"]/div[@id="listtyle1_w"]/div[@id="listtyle1_list"]//div[@class="listtyle1"]/a[@class="big"]/img[@class="img"]/@src').extract()
        for src in src_list:
            print(src)
            list1.append(src)
            item = FoodItem()
            item['image_urls'] = list1
            yield item
