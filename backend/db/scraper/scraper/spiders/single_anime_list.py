import scrapy
import json
from scrapy.selector import Selector 


# def single_anime_credentials(code, edition):
    # return  f"https://animixplay.to/v{edition}/{code}"
single_anime_credentials = lambda code, edition: f"https://animixplay.to/v{edition}/{code}"

class SingleAnimix(scraper.Spider):
    name = "singleanimix"
    
    def start_requests(self):
        url = single_anime_credentials
        
        yield scrapy.Requests(url=url, callback=self.parse)
        
    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'quotes-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
    

    