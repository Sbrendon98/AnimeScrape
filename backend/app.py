
from fastapi import FastAPI, Depends
from db import schema, models, db
from sqlalchemy.orm import Session

app = FastAPI()

@app.post("/")
def create(anime: schema.Anime_List_Base, db: Session = Depends(db.get_db)):
    creating = models.Anime_List(
        name = anime.name,
        isDubbed = False
    )
    db.add(creating)
    db.commit()
    return {
        "success": True,
        "created_id": creating.id
    }
@app.get("/")
async def get(id: int, db: Session = Depends(db.get_db)):
    return db.query(models.Anime_List)
    