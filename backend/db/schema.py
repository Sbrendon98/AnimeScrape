from pydantic import BaseModel

#Single Anime----------------------->
class AnimeBase(BaseModel):
    title: str
    episodes: int
    upcoming: str
    ongoing: bool

class AnimeCreate(AnimeBase):
    pass

class Anime(AnimeBase):
    id: int
    title_id: int
    
    class Config:
        orm_mode = True
#Single Anime---------------------->

#All Anime---------------------------->
class Anime_List_Base(BaseModel):
    title: str
    isDubbed: bool 
    edition: str
    
class Anime_List_Create(Anime_List_Base):
    pass

class Anime_List(Anime_List_Base):
    id: int

    class Config:
        orm_mode=True
#All Anime--------------------------->


#Favorites---------------------------->
class Anime_Favorites(BaseModel):
    title: str
    isFavorite: bool
    ongoing: bool
    upcoming: str

class Anime_Favorites_Create(Anime_Favorites):
    pass

class Anime_Favorites(Anime_Favorites):
    id: int

    class Config:
        orm_mode = True
#Favorites--------------------------->