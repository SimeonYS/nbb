import re

import scrapy

from scrapy.loader import ItemLoader
from ..items import NbbItem
from itemloaders.processors import TakeFirst
pattern = r'(\xa0)?'

class NbbSpider(scrapy.Spider):
	name = 'nbb'
	start_urls = ['https://www.nbb.be/nl/covid-19/ermg/persberichten-ermg']
	handle_httpstatus_list = [404]

	def parse(self, response):
		post_links = response.xpath('//div[@class="field-item even first"]//li//a/@href').getall()
		yield from response.follow_all(post_links, self.parse_post)

	def parse_post(self, response):

		date = response.xpath('//div[@class="field field-name-field-article-date field-type-datetime field-label-hidden"]/span//text()').get()
		date = re.findall(r'\d+\s\w+\s\d+', date)
		title = response.xpath('//h1/text()').get().strip()
		content = response.xpath('//div[@class="content"]//text()[not (ancestor::div[@class="group-related-content field-group-div"]) and not (ancestor::sup)]').getall()
		content = [p.strip() for p in content if p.strip()][1:]
		content = re.sub(pattern, "",' '.join(content))


		item = ItemLoader(item=NbbItem(), response=response)
		item.default_output_processor = TakeFirst()

		item.add_value('title', title)
		item.add_value('link', response.url)
		item.add_value('content', content)
		item.add_value('date', date)

		return item.load_item()
