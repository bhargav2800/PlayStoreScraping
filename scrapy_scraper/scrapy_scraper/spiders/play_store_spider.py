import scrapy

from play_store_scraper.models import GamesPath
from ..items import PlayStoreScrapperItem


class PlayStoreSpiderSpider(scrapy.Spider):
    name = "play_store_spider"
    allowed_domains = ["play.google.com"]
    start_urls = ["https://play.google.com/store/games?hl=en&amp;gl=US"]

    def parse(self, response):
        all_hrefs = response.css('.Si6A0c::attr(href)').getall()
        for href in all_hrefs:
            item = PlayStoreScrapperItem()
            item['app_detail_path'] = href
            GamesPath.objects.get_or_create(app_detail_path=href.split('?id=')[-1].split('&')[0])
            yield item
