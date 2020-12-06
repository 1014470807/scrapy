# -*- coding: utf-8 -*-
import scrapy
import re
from urllib.parse import urljoin
from scrapyProject.items import jinshi,jinItem
import time

class ScrapynameSpider(scrapy.Spider):
    name = 'jinshi'
    def start_requests(self):
        if jinshi.table_exists() == False:
            jinshi.create_table()
        yield scrapy.Request(url='https://www.jin10.com/', callback=self.parse_list)

    def parse_list(self, response):
        # yield CodeModel.delete().where(CodeModel.type == 2).execute()
        #prev_item = response.meta.get('jinItem')
        #print(prev_item)
        # print(response)
        for elem in response.css('.jin-flash-item-container'):
            # print(elem)
            # print(1111111111111111111111111111111111)
            # print(elem.css('.right-content > div::text').extract_first())
            # print(1111111111111111111111111111111111)
            # print(elem.css('.right-content > div::text').extract_first())
            item = jinItem()
            #item = {}
            if elem.css('.right-content > div::text').extract_first() == 0:
                break
            item['time'] = elem.css('.item-time::text').extract_first()
            item['createTime'] = int(round(time.time() * 1000))
            item['title'] = elem.css('.right-content > div::text').extract_first()
            try:
                if jinshi.select().where(jinshi.title == item['title']):
                    print(' ')
                else:
                    # print('插入有了数据')
                    jinshi.create(title=item['title'],time=item['time'],createTime=item['createTime'])
            except Exception as e:
                if str(e.args[0]) == '1062':
                    print ('重复数据，跳过。')
                else:
                    print (e.args[0],e.args[1])
            #item['url'] = elem.css('.tc:nth-child(2) > a::attr("href")').extract_first()
            # if prev_item is not None:
            #     for key, value in prev_item.items():
            #         item[key] = value
            yield item
