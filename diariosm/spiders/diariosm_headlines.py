# -*- coding: utf-8 -*-
import scrapy


class DiariosmHeadlinesSpider(scrapy.Spider):
    name = 'diariosm_headlines'
    allowed_domains = ['https://diariosm.com.br/']
    start_urls = ['http://https://diariosm.com.br/']

    def parse(self, response):
	
        pass
