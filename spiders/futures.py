# -*- coding: utf-8 -*-
import scrapy
import re
from urllib.parse import urljoin
from scrapyProject.items import tradingnews,tradingItem
import time
import json

class ScrapynameSpider(scrapy.Spider):
    name = 'futures'
    def start_requests(self):
        # if tradingnews.table_exists() == False:
        #     tradingnews.create_table() 加密货币
        yield scrapy.Request(url='https://cn.tradingview.com/markets/futures/ideas/', callback=self.parse_list)

    def parse_list(self, response):
        # yield CodeModel.delete().where(CodeModel.type == 2).execute()
        #prev_item = response.meta.get('tradingItem')
        #print(prev_item)
        # print(json.loads(response.text))

        # if rs.get('message') == 'success':
        # print(response.css('.tv-feed__item'))
        for elem in response.css('.tv-feed__item'):
            # print(elem)
            # print(1111111111111111111111111111111111)
            # print(elem.css('.right-content > div::text'))
            # print(1111111111111111111111111111111111)
            # print(elem.css('.right-content > div::text'))
            item = tradingItem()
            # print(elem.css('.tv-widget-idea__title-row::text'))
            #item = {}
            # print(elem.css('.tv-widget-idea__title-row > a:text').extract_first())
            if elem.css('.tv-widget-idea__title-row > a::text').extract_first() == 0:
                break
            item['time'] = int(round(time.time() * 1000))
            item['title'] = elem.css('.tv-widget-idea__title::text').extract_first()
            item['desc'] = elem.css('.tv-widget-idea__description-row::text').extract_first()
            item['author'] = elem.css('.tv-card-user-info__name::text').extract_first()
            item['img'] = elem.css('.tv-widget-idea__cover::attr(data-src)').extract_first()
            item['status'] = 4
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
            yield item

