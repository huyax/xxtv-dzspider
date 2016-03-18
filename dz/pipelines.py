# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb
import codecs
class DzPipeline(object):
    def process_item(self, item, spider):
        host='www.nxjsjwl.com'
	database='xxtv'
	username='xxtv'
	password='xxtv'
	self.conn = MySQLdb.connect(host,username,password,database)
	self.cursor = self.conn.cursor()
	self.conn.set_character_set('utf8')
        self.cursor.execute('SET NAMES utf8;')
        self.cursor.execute('SET CHARACTER SET utf8;')
        self.cursor.execute('SET character_set_connection=utf8;')
	#ids = get_id_list()
	#if(!ids.contains(item.id)):
	self.file = codecs.open('sql','wb',encoding='utf-8')
	self.insert(item)
	return item

    def get_id_list(self):
	sql = "select source_id from dz where source_website= '0' "

    def insert(self,item):
	sql = "insert into dz(author,content,c_create_date,source_postdate,comment_count,like_count) VALUES (%s,%s,%s,%s,%s,%s)"
	#sql = sql % (item['author'],item['content'],item['post_date'],item['post_date'],item['comment_count'],item['like_count'])
	print sql
	self.file.write(sql)
	self.cursor.execute(sql,(item['author'],item['content'],item['post_date'],item['post_date'],item['comment_count'],item['like_count']))
	self.conn.commit()
	print item['source_id'] + "insert done"
