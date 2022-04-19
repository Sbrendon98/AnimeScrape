from pydantic import BaseModel

class AnimeBase(BaseModel):
    name: str
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


class Anime_List_Base(BaseModel):
    name: str
    isDubbed: bool 
    edition: str
    
class Anime_List_Create(Anime_List_Base):
    pass

class Anime_List(Anime_List_Base):
    id: int
    
    class Config:
        orm_mode = True
    