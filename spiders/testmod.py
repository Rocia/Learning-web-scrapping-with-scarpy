# -*- coding: utf-8 -*-
import scrapy


class TestmodSpider(scrapy.Spider):
    name = 'testmod'
    allowed_domains = ['https://www.pulse.datamatics.com/dlintranet/Login.do?method=showLogout']
    start_urls = ['http://https://www.pulse.datamatics.com/dlintranet/Login.do?method=showLogout/']

    def parse(self, response):
        pass
