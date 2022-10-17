import scrapy 
import json
import request
from scraper.items import AnimeItem

anime_list = request.get()
class AnimixSpider(scrapy.Spider):
    name = "animix"
    
    def start_requests(self):
        urls = ['https://animixplay.to/assets/s/all.json']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):
        res = json.loads(response.text) 
        Items = AnimeItem()
        for id in range(len(res)):
            Items['title'] = res[id]['title']
            Items['code'] = res[id]['id']
            Items['edition'] = res[id]['e']
            yield Items
            