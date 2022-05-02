from sqlalchemy.orm import Session
import models, schema


#GET ALL ANIME
def get_anime_list():
    all_anime = Session.query(models.Anime_List).order_by(Anime_List.title).all()
    for anime in all_anime:
        print(f"Name: {anime.title}")
#GET ALL ANIME THAT ARE DUBBED

#GET ALL ANIME THAT ARE SUBBED

#GET FAVORITE ANIME
get_anime_list()


#ADD FAVORITE ANIME

#DELETE FAVORITE ANIME
