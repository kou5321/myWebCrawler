# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


#这里的两个函数get_media_requests和item_completed都是scrapy的内置函数，想重命名的就这这里操作
#可以直接复制这里的代码就可以用了
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy.http import Request


class MeizituPipeline(ImagesPipeline):
    def get_media_requests(self, item, info) :
        for image_url in item['image_urls'] :
            yield Request(image_url)

    def item_completed(self, results, item, info) :
        image_path = [x['path'] for ok, x in results if ok]
        if not image_path:
            raise DropItem('Item contains no images')
        item['image_paths'] = image_path
        return item