# -*- coding: utf-8 -*-
import scrapy


class TestmoSpider(scrapy.Spider):
    name = 'testmo'
    allowed_domains = ['www.pulse.datamatics.com/dlintranet/Login.do?method=showLogout']
    start_urls = ['http://www.pulse.datamatics.com/dlintranet/Login.do?method=showLogout/']

    def parse(self, response):
        pass
