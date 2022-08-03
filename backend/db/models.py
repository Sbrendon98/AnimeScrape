from operator import index
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from db.db import Base

#This is how we will be making our models.
#We define it as a class and make vairables with a Column function to categories each column in our database

class Anime_List(Base):
    __tablename__= "anime_list"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    code = Column(String, index=True, nullable=False)
    edition = Column(Integer, index=True)
#nullable is to make sure that the data being passed to the name Column cannot be null
    isDubbed = Column(Boolean, default=False)
    anime = relationship("Anime", back_populates="anime_list")
    
    def __repr__(self):
        return f"id={self.id},title={self.title},edition={self.edition},isDubbed={self.isDubbed}"

class Anime(Base):
    __tablename__="anime"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    episodes = Column(Integer, index=True)
    upcoming = Column(String, index=True)
    ongoing = Column(Boolean, index=True)
    title_id = Column(Integer, ForeignKey("anime_list.id"))
    
    anime_list = relationship("Anime_List", back_populates="anime")
    def __repr__(self):
        return f"id={self.id},title={self.title},episodes={self.episodes},upcoming={self.upcoming},ongoing={self.ongoing}"
