import scrapy

from pep_parse.constants import ALLOWED_DOMAINS, START_URLS
from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ALLOWED_DOMAINS
    start_urls = START_URLS

    def parse(self, response):
        all_href = response.css('section#numerical-index').css(
            'tbody').css('a::attr(href)').getall()
        for href in all_href:
            yield response.follow(href, callback=self.parse_pep)

    def parse_pep(self, response):
        title = response.css('h1.page-title::text')
        status = response.css('dt:contains("Status") + dd')
        data = {
            'number': int(title.get().split(sep=' ')[1]),
            'name': title.get().split(sep='– ')[1],
            'status': status.css('abbr::text').get(),
        }
        yield PepParseItem(data)
