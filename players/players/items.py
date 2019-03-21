# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Fixture(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    tournament = scrapy.Field()
    date = scrapy.Field()
    team_home = scrapy.Field()
    team_away = scrapy.Field()
    score = scrapy.Field()
    minutes = scrapy.Field()
    rating = scrapy.Field()
#    pass
