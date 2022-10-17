
from fastapi import FastAPI, Depends, status
from db import schema, models, db
from sqlalchemy.orm import Session
from typing import Optional, List
from db.scraper.scraper.spiders.single_anime_list import single_anime_credentials
import requests

SessionLocal = db.SessionLocal()
app = FastAPI()

# @app.post("/")
# def create(anime: schema.Anime_List_Base, db: Session = Depends(db.get_db)):
    # creating = models.Anime_List(
        # name = anime.name,
        # isDubbed = False
#)
# db.add(creating)
# db.commit()
# return {
#     "success": True,
#     "created_id": creating.id
# }
#@app.get("/")
#async def get(id: int, db: Session = Depends(db.get_db)):
    #return db.query(models.Anime_List)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/allAnime", response_model=List[schema.Anime_List], status_code=200)
def get_all_anime():
    allAnime = SessionLocal.query(models.Anime_List).all()
    return allAnime

#This API request needs to call the scrapy command to make the query. 
@app.get("/allAnime/{anime_id}", status_code=200)
def get_single_anime(anime_id: int,):
    singleAnime = SessionLocal.query(models.Anime_List).filter(models.Anime_List.id ==anime_id).first()
    return singleAnime
    #data = single()
    #for key, value in data.__dict__.iteritems():
    #    print(key, value)
    #for data in single:
    #   pass
    #req = requests.post("http://127.0.0.1:8000/singleAnime" , data={"code": data['code'], "edition": data['edition']})
    #return req
    # print(singleAnime.__dict__["title"])

@app.post("/singleAnime/{anime_id}", response_model=schema.Anime, status_code=201 )
def create_single_anime(anime: schema.Anime):
    createAnime = SessionLocal.query(models.Anime_List).filter(models.Anime_List.id == anime_id),first()
    code = createAnime.__dict__["code"]
    edition = createAnime.__dict__["edition"]
    #This will become an object that will be passed into the single Anime schema
    credentials = single_anime_credentials(code, edition)
    #This is where the payload will be passed to the model and uploaded to the database
    new_anime = models.Anime(
        id,
        title,
        episodes,
        upcoming,
        ongoing
    )
    
#This will change is Favorites to True

@app.put("/allAnime/{anime_id}")
async def update_single_anime(id):
    pass

@app.get("/allAnime/favorites")
async def get_favorite_anime():
    pass