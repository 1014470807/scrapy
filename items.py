# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from peewee import *

db = MySQLDatabase("news",host='106.54.53.151',port=3306,user='root', passwd='QQdulagesi520gg!', charset='utf8')

class Item(scrapy.Item):
    code = scrapy.Field()
    codeName = scrapy.Field()
    continuityDay = scrapy.Field()
    industry = scrapy.Field()
    type = scrapy.Field()

class CodeModel(Model):
    # one 是主键
    #code = CharField(verbose_name="code", max_length=100, primary_key=True, null=False)
    code = CharField(verbose_name="code", max_length=6, null=False)
    codeName = CharField(verbose_name="codeName", max_length=30, null=False)
    continuityDay = CharField(verbose_name="continuityDay",max_length=4, null=False)
    industry = CharField(verbose_name="industry",max_length=30, null=False)
    type = CharField(verbose_name="type",max_length=10, null=False)

    class Meta:
        database = db


class jinItem(scrapy.Item):
    title = scrapy.Field()
    time = scrapy.Field()
    createTime = scrapy.Field()

class jinshi(Model):
    # one 是主键
    #code = CharField(verbose_name="code", max_length=100, primary_key=True, null=False)
    title = CharField(verbose_name="title")
    time = CharField(verbose_name="time", max_length=30, null=False)
    createTime = CharField(verbose_name="createTime",max_length=30, null=False)

    class Meta:
        database = db

class tradingItem(scrapy.Item):
    title = scrapy.Field()
    desc = scrapy.Field()
    time = scrapy.Field()
    author = scrapy.Field()
    img = scrapy.Field()
    status = scrapy.Field()

class tradingnews(Model):
    # one 是主键
    #code = CharField(verbose_name="code", max_length=100, primary_key=True, null=False)
    title = CharField(verbose_name="title")
    desc = CharField(verbose_name="desc")
    time = CharField(verbose_name="time", max_length=30, null=False)
    author = CharField(verbose_name="author",max_length=30, null=False)
    img = CharField(verbose_name="img")
    status = CharField(verbose_name="status",max_length=10, null=False)

    class Meta:
        database = db
