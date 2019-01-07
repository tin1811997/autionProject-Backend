from sqlalchemy import create_engine  
from sqlalchemy import Column, String  
from sqlalchemy.ext.declarative import declarative_base  
from sqlalchemy.orm import sessionmaker

db_string = "postgresql://nguyentin:123456@localhost:5433/test1"

db = create_engine(db_string)  
base = declarative_base()
class Film(base):  
    __tablename__ = 'films'

    title = Column(String, primary_key=True)
    director = Column(String)
    year = Column(String)

Session = sessionmaker(db)  
session = Session()




films = session.query(Film)  
for film in films:  
    print(film.title)
