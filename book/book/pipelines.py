# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import requests
import os
import pymysql

db = pymysql.connect(host = "localhost",port = 3306, user = "root",password =  "", db = "bookstore",charset='utf8')

class BookPipeline(object):
    def process_item(self, item, spider):
        print("+"*10)
        print("hello, pipline")
        try:
            os.mkdir("D:\PictureList")
        except:
            print("创建文件失败")
        for i in range(1, min(len(item['title']), len(item['pic']), len(item['price']), len(item['author']), len(item['time']), len(item['publish']))):
            title = item['title'][i]
            price = item['price'][i]
            pic = item['pic'][i-1]
            author = item['author'][i]
            publish = item['publish'][i]
            time = item['time'][i]

            
            cursor = db.cursor()
            
            name = "D:/PictureList/" + pic[-18:]

            cursor = db.cursor()
            sql = """ insert into booklist (title, price, pic, author, publish, time, picpath) values(%s, %s, %s, %s, %s, %s,  %s)"""
            cursor.execute(sql, (title, price, pic, author, publish, time, name))
            db.commit()


            picT = requests.get(pic).content
           
            

            name = "D:/PictureList/" + pic[-18:] 

            with open(name , 'wb') as f:
                f.write(picT)   
            

        return item
