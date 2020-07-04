# -*- coding: utf-8 -*-
import scrapy
from ..items import Meizitu2Item
from scrapy.crawler import CrawlerProcess


class GirlspiderSpider(scrapy.Spider):
    name = 'girlSpider'
    allowed_domains = ['http://www.jandan.net/ooxx']
    start_urls = ['http://www.jandan.net/ooxx/', ]

    # def parse(self, response):
    #     item = Meizitu2Item
    #     item['image_urls'] = response.xpath('//img//@src').extract()#提取图片链接
    #     # print ‘image_urls‘,item[‘image_urls‘]
    #     yield item
    #     new_url = response.xpath('//a[@class="previous-comment-page"]//@href').extract_first()#翻页
    #     # print ‘new_url‘,new_url
    #     if new_url:
    #         yield scrapy.Request(new_url, callback=self.parse)
    def parse(self, response):
        list1 = []
        src_list = response.xpath('/html/body/div[@id="wrapper"]/div[@id="body"]/div[@id="content"]/div[@id="comments"]/ol[@class="commentlist"]//li/div/div[@class="row"]/div[@class="text"]/p/img/@src').extract()
        for src in src_list:
            src1 = "http:" + src
            item = Meizitu2Item()
            list1.append(src1)
            item['image_urls'] = list1
            yield item
            
