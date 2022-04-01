from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#This is how we will be making the connection to the database
engine = create_engine('postgresql+psycopg2://postgres:admin@localhost:5432/anime_scrape')

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine )
#declarative base makes a connection to our db models
Base = declarative_base()
#This is how we will retrieve the database session an use it through our project
def get_db():
    db = SessionLocal
    try:
        yield db
    except:
        db.close()
    
