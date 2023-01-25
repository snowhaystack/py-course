from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sqlalchemy as db

DB_CONN = "sqlite:///./novatag.db"
engine = db.create_engine(DB_CONN, echo=True)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()
