import json

def animeFile():
    list = open('animelist.json')
    anime = json.load(list)
    return anime
