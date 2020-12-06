# -*- coding: utf-8 -*-
import scrapy
import re
from urllib.parse import urljoin
import pymysql
from scrapyProject.items import Item,CodeModel

class ScrapynameSpider(scrapy.Spider):
    name = 'codeLiang'
    def start_requests(self):
        if CodeModel.table_exists() == False:
            CodeModel.create_table()
        yield scrapy.Request(url='http://data.10jqka.com.cn/rank/ljqd/', callback=self.parse_list)

    def parse_list(self, response):
        yield CodeModel.delete().where(CodeModel.type == 2).execute()
        prev_item = response.meta.get('item')
        for elem in response.css('table tbody tr'):
            item = Item()
            #item = {}
            # print(111111111111111111111)
            # print(elem.css('.tc:nth-child(2) > a::text').extract_first())
            # print(111111111111111111111)
            item['code'] = elem.css('.tc:nth-child(2) > a::text').extract_first()
            item['codeName'] = elem.css('.tc:nth-child(3) > a::text').extract_first()
            item['continuityDay'] = elem.css('.tc:nth-child(5)::text').extract_first()
            item['industry'] = elem.css('.tc:nth-child(8) > a::text').extract_first()
            item['type'] = 2
            try:
                CodeModel.create(code=item['code'],codeName=item['codeName'],continuityDay=item['continuityDay'],industry=item['industry'],type=item['type'])
            except Exception as e:
                if str(e.args[0]) == '1062':
                    print ('重复数据，跳过。')
                else:
                    print (e.args[0],e.args[1])
            #item['url'] = elem.css('.tc:nth-child(2) > a::attr("href")').extract_first()
            if prev_item is not None:
                for key, value in prev_item.items():
                    item[key] = value
            yield item
