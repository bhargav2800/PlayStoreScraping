# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
import scrapy

class PlayStoreScrapperItem(scrapy.Item):
    app_detail_path = scrapy.Field()
