# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SongCrawlerItem(scrapy.Item):
	title = scrapy.Field()
	song = scrapy.Field()
	lyricist = scrapy.Field()
	singer = scrapy.Field()
	composer = scrapy.Field()
	genre = scrapy.Field()