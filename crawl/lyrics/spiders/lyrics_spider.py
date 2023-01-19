import scrapy
from lyrics.items import SongCrawlerItem
import re


class SongSpider(scrapy.Spider):
	name = "lyrics"

	# First Start Url
	start_urls = ["https://www.sinhalasongbook.com/all-sinhala-song-lyrics-and-chords/"]

	# This mimics getting the pages using the next button. 
	pages = 6
	for i in range(2, pages):
		start_urls.append("https://www.sinhalasongbook.com/all-sinhala-song-lyrics-and-chords/?_page="+str(i)+"")
	
	def parse(self, response):
		for href in response.xpath("//h4[contains(@class, 'pt-cv-title')]/a[contains(@class,'_blank')]//@href").extract():
			yield scrapy.Request(href, callback=self.parse_dir_contents)
					
	def parse_dir_contents(self, response):
		item = SongCrawlerItem()

		# Song title
		item['title'] = response.xpath("//h1[contains(@class, 'entry-title')]/descendant::text()").extract()[0].strip()

		# Extract lyrics
		lyrics = response.css("pre ::text").getall()
		formatted_lyrics = ''
		for i in range(len(lyrics)):
			updated_string = re.sub(r'[a-zA-Z]|\d|#|[\([{})\]]|-|,|∆|—|\/|\'|\|+|', '', lyrics[i])
			updated_strings = re.sub(r'\s+', ' ', updated_string).strip()
			formatted_lyrics += updated_strings

		# Extract and assign elements
		item['song'] = formatted_lyrics
		item['lyricist'] = response.xpath("//span[contains(@class, 'lyrics')]/a/text()").extract()[0].strip()
		item['singer'] = response.xpath("//span[contains(@class, 'entry-categories')]/a/text()").extract()[0].strip()
		item['composer'] = response.xpath("//span[contains(@class, 'music')]/a/text()").extract()[0].strip()
		item['genre'] = response.css("div.su-column-inner span.entry-tags a ::text").getall()

		# Filter by genre 'pop'
		for genre in response.css("div.su-column-inner span.entry-tags a ::text").getall():
			if "pop".lower() in genre.lower():
				yield item