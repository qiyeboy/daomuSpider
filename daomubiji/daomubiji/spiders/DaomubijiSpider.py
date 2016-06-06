#coding:utf-8
import scrapy
from scrapy.selector import Selector
from daomubiji.items import DaomubijiItem


class daomuSpider(scrapy.Spider):
    name = "daomu"
    allowed_domains = ["seputu.com"]
    start_urls = ["http://seputu.com/"]
    ''.split()

    def parse(self, response):
        selector = Selector(response)
        mulus= selector.xpath("//div[@class='mulu']/div[@class='mulu-title']/center/h2/text()").extract()#将目录提取出来
        boxs = selector.xpath("//div[@class='mulu']/div[@class='box']")#.extract()
        for i in range(len(mulus)):
            mulu = mulus[i]#提取出来一个目录
            box = boxs[i]#提取出来一个box
            texts = box.xpath(".//ul/li/a/text()").extract()#将文本提取出来
            urls  = box.xpath(".//ul/li/a/@href").extract()#将链接提取出来
            for j in range(len(urls)):
                item = DaomubijiItem()
                item['bookName'] = mulu
                try:
                    item['bookTitle'] = texts[j].split(' ')[0]
                    item['chapterNum'] = texts[j].split(' ')[1]
                    item['chapterName'] = texts[j].split(' ')[2]
                    item['chapterUrl'] = urls[j]
                    request = scrapy.Request(urls[j],callback=self.parseBody)
                    request.meta['item'] = item
                    yield request


                except Exception,e:
                    print 'excepiton',e
                    continue



    def parseBody(self,response):
        '''
        解析小说章节中的内容
        :param response:
        :return:
        '''
        item = response.meta['item']
        selector = Selector(response)

        item['chapterContent'] ='\r\n'.join(selector.xpath("//div[@class='content-body']/p/text()").extract())
        yield item