# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DaomubijiItem(scrapy.Item):
    # define the fields for your item here like:
    bookName = scrapy.Field()#书籍的名字
    bookTitle = scrapy.Field()#书籍的标题
    chapterNum = scrapy.Field()#书的章节
    chapterName = scrapy.Field()#章节的名称
    chapterUrl = scrapy.Field()#章节的url
    chapterContent = scrapy.Field()#章节的内容
    pass
