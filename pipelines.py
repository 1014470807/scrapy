# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
from scrapyProject.items import CodeModel,jinshi

class ScrapyprojectPipeline(object):

    def process_item(self, item, spider):
        # if CodeModel.table_exists() == False:
        #     CodeModel.create_table()
        # try:
        #     CodeModel.create(code=item['code'],codeName=item['codeName'],continuityDay=item['continuityDay'],industry=item['industry'],type=item['type'])
        # except Exception as e:
        #     if str(e.args[0]) == '1062':
        #         print ('重复数据，跳过。')
        #     else:
        #         print (e.args[0],e.args[1])

        return item

    # def process_item(self, item, spider):
    #     if jinshi.table_exists() == False:
    #         jinshi.create_table()
    #     try:
    #         # print("123")
    #         # print(jinshi.select().where(jinshi.title == item['title']))
    #         if jinshi.select().where(jinshi.title == item['title']):
    #             print(' ')
    #         else:
    #             jinshi.create(title=item['title'],time=item['time'],createTime=item['createTime'])
    #     except Exception as e:
    #         if str(e.args[0]) == '1062':
    #             print ('重复数据，跳过。')
    #         else:
    #             print (e.args[0],e.args[1])
    #
    #     return item

    def open_spider(self, spider):
        self.client = pymysql.Connect(
            host='106.54.53.151',
            port=3306,
            user='root',
            passwd='QQdulagesi520gg!',
            db='news',
            charset='utf8'
        )

    # def process_item(self, item, spider):
    #     print(item)
    #     print("成功")
    #     self.client.cursor().execute("insert into code (code,codeName,continuityDay,industry,type) values (%s)", (item["code"],item["codeName"],item["continuityDay"],item["industry"],item["type"]))
    #     self.client.commit()
    #     return item

    def close_spider(self, spider):
        self.client.close()
