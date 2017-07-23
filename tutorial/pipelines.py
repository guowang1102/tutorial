# -*- coding: utf-8 -*-
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy import signals
# import json
# import codecs
#
#
# class JsonWithEncodingTencentPipeline(object):
#     def __init__(self):
#         self.file = codecs.open('1024.txt', 'w', encoding='utf-8')
#
#     def process_item(self, item, spider):
#         line = json.dumps(dict(item), ensure_ascii=False) + "\n"
#         self.file.write(line)
#         return item
#
#     def spider_closed(self, spider):
#         self.file.close()
import pymysql

def dbHandle():
    connect = pymysql.Connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='root',
        db='python',
        charset='utf8'
    )
    return connect

class HelloPipeline(object):
    def process_item(self, item, spider):
        dbObject = dbHandle()
        cursor = dbObject.cursor()
        sql = 'insert into fid3(name) values (%s)'
        try:
            cursor.execute(sql,(item['title']))
            dbObject.commit()
        except Exception,e:
            print e
            dbObject.rollback()
        return item

