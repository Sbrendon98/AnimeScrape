
from fastapi import FastAPI, Depends
from db import schema, models, db
from sqlalchemy.orm import Session
from typing import Optional, List

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
async def get_all_anime():
    allAnime = SessionLocal.query(models.Anime_List).all()
    return allAnime

#This API request needs to call the scrapy command to make the query. 
@app.post("/allAnime/{id}")
async def create_single_anime(id: int):
    single = SessionLocal
#This will change is Favorites to True
@app.put("/allAnime/{id}")
async def update_single_anime(id):
    pass

@app.get("/allAnime/favorites")
async def get_favorite_anime():
    pass