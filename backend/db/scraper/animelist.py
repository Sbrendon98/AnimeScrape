import json

def animeFile():
    list = open('backend\db\scraper\\animelist.json')
    anime = json.load(list)
    return anime