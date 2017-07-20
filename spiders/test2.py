# -*- coding: utf-8 -*-
import scrapy


class Test2Spider(scrapy.Spider):
    name = 'test2'
    allowed_domains = ['http://inviewapp.cch.com/lbautolog/Pages/LogSearch.aspx']
    start_urls = ['http://http://inviewapp.cch.com/lbautolog/Pages/LogSearch.aspx/']

    def parse(self, response):
        pass
