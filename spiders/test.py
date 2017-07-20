# -*- coding: utf-8 -*-
import scrapy


class TestSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['http://Sakthivel.J:Pass@2511@inviewapp.cch.com/lbautolog/Pages/LogSearch.aspx']
    start_urls = ['http://http://Sakthivel.J:Pass@2511@inviewapp.cch.com/lbautolog/Pages/LogSearch.aspx/']

    def parse(self, response):
        pass
