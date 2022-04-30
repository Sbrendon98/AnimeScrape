import json
from sqlalchemy.orm import Session
import models, schema

file = r"/mnt/c/Users/Ashton/Senior Phase Project/AnimeSpider/backend/db/scraper/animelist.json"
def animeFile():
    list = open(file,"r")
    anime = json.load(list)
    return anime

def create_anime_list(db: Session, animeList: schema.Anime_List_Create):
    db_anime_list = models.Anime_List(title=animeList.title,code=animeList.code, edition=animeList.edition, isDubbed=False)
    db.add(db_anime_list)
    db.commit()
    db.refresh(db_anime_list)
    return db_anime_list

def get_anime_list(db: Session, id: int):
    return db.query(models.Anime_List).all()




