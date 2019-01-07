import os
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv

# Load Dotenv from .env file
load_dotenv()

Base = declarative_base()

# Create engine from Server to DB
engine = create_engine(os.getenv("DBURL"))

# Setup Session base on that's engine
db_session = scoped_session(sessionmaker(autocommit=False,autoflush=False,bind=engine))
# Session = sessionmaker(engine)
# session = Session()