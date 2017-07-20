# -*- coding: utf-8 -*-
import scrapy


class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['https://doc.scrapy.org/en/latest/topics/commands.html']
    start_urls = ['http://https://doc.scrapy.org/en/latest/topics/commands.html/']

    def parse(self, response):
        pass
