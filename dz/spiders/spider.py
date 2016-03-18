# -*- coding: utf-8 -*-

import scrapy
import codecs
import json
import sys
from dz.items import DzItem
reload(sys)
sys.setdefaultencoding("utf-8")

class QiushibaikeSpider(scrapy.Spider):
    name = 'dz'
    start_urls = ['http://www.qiushibaike.com/hot/']
    headers = {
	"Host":"www.qiushibaike.com",
	"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
	"Accept-Encoding":"gzip, deflate, sdch",
	"Accept-Language":"zh-CN,zh;q=0.8",
	"Upgrade-Insecure-Requests":"1",
	"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36"
    }

    def start_requests(self):
	self.file = codecs.open('data.json','wb',encoding='utf-8')
	yield scrapy.Request(url=self.start_urls[0],headers=self.headers,callback=self.parse_titles)

    def parse_titles(self, response):
	items = []
        for sel in response.xpath('//div[@class="col1"]/div[@class="article block untagged mb15"]'):
            item = DzItem()
	    item['source_id'] = sel.xpath('.//@id').extract()[0].decode("utf-8")
	    contents = sel.xpath('.//div[@class="content"]/text()').extract()
	    #print item['content']
	    content_utf8 = ''
	    for content in contents:
		print content
		content_utf8= content_utf8 + content.decode("utf-8")
	    item['content'] = content_utf8
	    # 需要判断是否是注册用户或者是匿名用户，现在的判断方法有问题，暂时屏蔽了，全部用匿名用户代替
	    #author = sel.xpath('.//div[@class="author clearfix"]/a/img/@alt').extract()
	    #if len(author) > 0:
		#author = author[0].decode("utf-8")
	    #else:
		#author = ''
	    item['author'] = '匿名用户'
	    # 糗事百科上面的段子都没有发表时间，暂时没有找到，随便用了一个日期
	    item['post_date'] = '2016-01-11'
	    item['like_count'] = sel.xpath('.//div[@class="stats"]/span[@class="stats-vote"]/i[@class="number"]/text()').extract()[0].decode("utf-8")
	    item['comment_count'] = sel.xpath('.//div[@class="stats"]/span[@class="stats-comments"]/a/i[@class="number"]/text()').extract()[0].decode("utf-8")

            #self.file.write(item['content'].decode('utf-8'))
	    items.append(item)
	return items

