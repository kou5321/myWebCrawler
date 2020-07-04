# -*- coding: utf-8 -*-
import scrapy
# import bs4
from ..items import MeizituItem


class BeautyspiderSpider(scrapy.Spider):
    name = 'beautySpider'
    allowed_domains = ['sohu.com']
    start_urls = ['http://www.sohu.com/a/337634404_100032610']

    def parse(self, response):
        item = MeizituItem()
        # srcs = response.css('.article img::attr(src)').extract()  # 看一下css提取
        srcs = response.xpath('/html/body/div[@class="wrapper-box"]/div[@id="article-container"]/div[@class="left main"]/div[1]/div[@class="text"]/article[@id="mp-editor"]/p/img/@src').extract()
        print(srcs)
        item['image_urls'] = srcs
        yield item
    
    # def parse(self, response):
    #     # item = MeizituItem()
    #     bs = bs4.BeautifulSoup(response.text, 'html.parser')
    #     article = bs.find('article', class_="article")
    #     tag_p = article.find_all('p')
    #     if tag_p.find("img"):
    #         pics = tag_p.find("img")
    #         for pic in pics:
    #             item = MeizituItem
    #             item['image_urls'] = pic["src"]
    #             yield item
