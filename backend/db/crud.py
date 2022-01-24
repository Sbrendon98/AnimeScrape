from sqlalchemy.orm import Session

import models, schema

def get_anime_list(db: Session, id: int):
    return db.query(models.Anime_List).all()

#def get_anime(db:Session, )

def create_anime_list(db: Session, animeList: schema.Anime_List_Create):
    db_anime_list = models.Anime_List(name=animeList.name, isDubbed=False)
    db.add(db_anime_list)
    db.commit()
    db.refresh(db_anime_list)
    return db_anime_list