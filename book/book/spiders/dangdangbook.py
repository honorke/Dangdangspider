# -*- coding: utf-8 -*-
#git test

import scrapy
from book.items import BookItem
from scrapy.http import Request



class DangdangbookSpider(scrapy.Spider):
    name = 'dangdangbook'
    allowed_domains = ['dangdang.com']
    start_urls = ['http://search.dangdang.com/?key=%BC%C6%CB%E3%BB%FA&act=input']

    def parse(self, response):
        print("-"*10)
        #print("hello, world")
        item = BookItem()
        item['title'] = response.xpath("//a[@class='pic']/@title").extract()
        item['price'] = response.xpath("//span[@class='search_now_price']/text()").extract()
        item['pic'] = response.xpath("//a[@class='pic']/img/@data-original").extract()


        
        item['author'] = response.xpath("//a[@name='itemlist-author']/text()").extract()
        item['publish'] = response.xpath("//a[@name='P_cbs']/@title").extract()
        item['time'] = response.xpath("//p[@class='search_book_author']/span[2]/text()").extract()

        yield item
        for i in range(1, 6):
            url = "http://search.dangdang.com/?key=%BC%C6%CB%E3%BB%FA&act=input&page_index="+str(i)
            yield Request(url, callback=self.parse)

        
