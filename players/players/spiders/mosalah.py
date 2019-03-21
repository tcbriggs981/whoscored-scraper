# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from players.items import Fixture

# Handling re-captcha blocks.
from incapsula import IncapSession, RecaptchaBlocked
session = IncapSession()
try:
    response = session.get('http://www.whoscored.com/')
except RecaptchaBlocked as e:
    raise

class SalahSpider(scrapy.Spider):
    name = "mosalah"
    allowed_domains = ["whoscored.com"]
    start_urls = (
                  'http://www.whoscored.com/',
                  )
        
    def parse(self, response):
        return Request(
                       url="https://www.whoscored.com/Players/108226/Fixtures/Mohamed-Salah",
                       callback=self.parse_fixtures
                       )

    def parse_fixtures(self,response):
        sel = response.selector
        for tr in sel.css("table#player-fixture>tbody>tr"):
            item = Fixture()
            item['tournament'] = tr.xpath('td[@class="tournament"]/span/a/text()').extract()
            item['date'] = tr.xpath('td[@class="date"]/text()').extract()
            item['team_home'] = tr.xpath('td[@class="team home "]/a/text()').extract()
            item['team_away'] = tr.xpath('td[@class="team away "]/a/text()').extract()
            item['score'] = tr.xpath('td[@class="result"]/a/text()').extract()
            item['minutes'] = tr.xpath('td[@class="info"]/a/text()').extract()
            item['rating'] = tr.xpath('td[@class="rating"]/a/text()').extract()
            yield item
