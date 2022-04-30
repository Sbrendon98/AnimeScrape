import json
from db import SessionLocal
import models
import re

local_session=SessionLocal()

file = r"/mnt/c/Users/Ashton/Senior Phase Project/AnimeSpider/backend/db/scraper/animelist.json"

def animeFile():
    list = open(file,"r")
    anime = json.load(list)
    return anime

for anime in animeFile():
    dub = re.search("(Dub)", anime["title"])
    new_anime = models.Anime_List(
        title=anime["title"],
        code=anime["code"],
        edition=anime["edition"],
        isDubbed=True if dub else False
        )
    local_session.add(new_anime)
    local_session.commit()