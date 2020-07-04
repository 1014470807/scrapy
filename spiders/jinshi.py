# -*- coding: utf-8 -*-
import scrapy
import re
from urllib.parse import urljoin
from scrapyProject.items import jinshi,jinItem
import time

class ScrapynameSpider(scrapy.Spider):
    name = 'jinshi'
    def start_requests(self):
        yield scrapy.Request(url='https://www.jin10.com/', callback=self.parse_list)

    def parse_list(self, response):
        # yield CodeModel.delete().where(CodeModel.type == 2).execute()
        #prev_item = response.meta.get('jinItem')
        #print(prev_item)
        for elem in response.css('.jin-flash_item'):
            item = jinItem()
            #item = {}
            if elem.css('.jin-flash_b > h4::text').extract_first() == 0:
                break
            item['time'] = elem.css('.jin-flash_time::text').extract_first()
            item['createTime'] = int(round(time.time() * 1000))
            item['title'] = elem.css('.jin-flash_b > h4::text').extract_first()
            #item['url'] = elem.css('.tc:nth-child(2) > a::attr("href")').extract_first()
            # if prev_item is not None:
            #     for key, value in prev_item.items():
            #         item[key] = value
            yield item