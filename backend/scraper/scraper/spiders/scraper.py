
# from bs4 import BeautifulSoup
# from selenium import webdriver
# from selenium.webdriver import Chrome
# from selenium.webdriver.chrome.options import Options
# # from requests_html import HTMLSession
# import requests
# import time
# #This is to handle the first line of defense. DISCLAMINER: I do not condone the use of this negatively. Do this at your own risk. This is just for educational purposes
# headers = requests.utils.default_headers()
# headers.update({
#     'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:12.0) Gecko/20100101 Firefox/12.0'
# })
# url = '
# data = requests.get(url, headers=headers)
# print(data)
# # session = HTMLSession()

# # res = session.get(url, headers=headers)
# # res.html.render()
# # html = res.html.html
# chrome_options = Options()
# chrome_options.add_argument("--headless")

# with Chrome(options=chrome_options) as browser:
#     browser.get(data)
#     html = browser.page_source
# soup = BeautifulSoup(html, "html.parser")

# containers = soup.find_all("div", {"class": "allitem"})
# print(soup)
# # print(html.body.find("div", "middle").find("div", "leftside").find("listplace"))
# # for div in html.find_all("div"):
# #     print(div.text)

# # allitem = html.find("div", "listplace")
# # print(allitem)

import scrapy 

class AnimixSpider(scrapy.Spider):
    name = "animix"
    
    def start_requests(self):
        urls = ['https://web.archive.org/web/20211211123510/https://animixplay.to/list']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):
        
        page = response.url.split("/")[-2]
        filename = f'quotes-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')
            