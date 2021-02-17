# -*- coding: utf-8 -*-
import scrapy
import re
from urllib.parse import urljoin
from scrapyProject.items import tradingnews,tradingItem
import time
import json

class ScrapynameSpider(scrapy.Spider):
    name = 'trading'
    def start_requests(self):
        # if tradingnews.table_exists() == False:
        #     tradingnews.create_table()
        print(12333333333333333333333333333333333333333)
        yield scrapy.Request(url='https://news-headlines.tradingview.com/headlines/?category=base&client=web&country=CN&lang=zh-Hans&locale=zh_CN', callback=self.parse_list)

    def parse_list(self, response):
        # yield CodeModel.delete().where(CodeModel.type == 2).execute()
        #prev_item = response.meta.get('tradingItem')
        #print(prev_item)
        # print(json.loads(response.text))

        # if rs.get('message') == 'success':
        for elem in json.loads(response.text):
            # print(elem)
            # print(1111111111111111111111111111111111)
            # print(elem.css('.right-content > div::text'))
            # print(1111111111111111111111111111111111)
            # print(elem.css('.right-content > div::text'))
            item = tradingItem()
            #item = {}
            if elem.get('title') == 0:
                break
            item['time'] = int(round(time.time() * 1000))
            item['title'] = elem.get('title')
            item['desc'] = elem.get('shortDescription')
            item['author'] = elem.get('source')
            item['img'] = ''
            item['status'] = 1
            try:
                if tradingnews.select().where(tradingnews.title == item['title']):
                    print('')
                else:
                    tradingnews.create(title=item['title'],time=item['time'],desc=item['desc'],author=item['author'],img=item['img'],status=item['status'])
            except Exception as e:
                if str(e.args[0]) == '1062':
                    print ('重复数据，跳过。')
                else:
                    print ('ok')
            #item['url'] = elem.css('.tc:nth-child(2) > a::attr("href")')
            # if prev_item is not None:
            #     for key, value in prev_item.items():
            #         item[key] = value
            yield item

