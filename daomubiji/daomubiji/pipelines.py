# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
from scrapy.pipelines.files import FilesPipeline
from daomubiji import settings
from pymongo import MongoClient

class DaomubijiPipeline(object):
    def process_item(self, item, spider):#将小说进行存储
        dir_path = '%s/%s/%s'%(settings.FILE_STORE,spider.name,item['bookName']+'_'+item['bookTitle'])#存储路径
        print 'dir_path',dir_path
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        file_path = '%s/%s'%(dir_path,item['chapterNum']+'_'+item['chapterName']+'.txt')
        with open(file_path,'w') as file_writer:
            file_writer.write(item['chapterContent'].encode('utf-8'))
            file_writer.write('\r\n'.encode('utf-8'))

        file_writer.close()
        return item

class DaomuSqlPipeline(object):

    def __init__(self):
    #连接mongo数据库,并把数据存储
        client = MongoClient()#'mongodb://localhost:27017/'///'localhost', 27017///'mongodb://tanteng:123456@localhost:27017/'
        db = client.daomu
        self.books = db.books

    def process_item(self, item, spider):
        print 'spider_name',spider.name
        temp ={'bookName':item['bookName'],
               'bookTitle':item['bookTitle'],
               'chapterNum':item['chapterNum'],
               'chapterName':item['chapterName'],
               'chapterUrl':item['chapterUrl']
               }
        self.books.insert(temp)

        return item
