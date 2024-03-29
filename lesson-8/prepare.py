# SQLAchemy
from pydantic import BaseModel
from fastapi import FastAPI
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sqlalchemy as db
import datetime
import random

Base = declarative_base()
DB_CONN = "sqlite:///./core.db"

# create mapping table for receipt


class Receipt(Base):
    __tablename__ = "receipt"
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    desc = db.Column('desc', db.Text)
    amount = db.Column('amount', db.Integer)
    data = db.Column('date', db.Date)

    def __str__(self) -> str:  # for print result
        return f"({self.id}) {self.desc} in data {self.data} -> € {self.importo}"

    def __repr__(self):
        return f"({self.id}) {self.desc} in data {self.data} -> € {self.importo}"


# init db connection
engine = db.create_engine(DB_CONN, echo=True)
# create tables
Base.metadata.create_all(engine)
# session init
Session = sessionmaker(bind=engine)
session = Session()
# -----------
receipt1 = Receipt()
receipt1.desc = 'decription'
receipt1.amount = random.randint(57, 500)
receipt1.data = datetime.date(
    2023, random.randint(1, 12), random.randint(1, 28))
# -----------
session.add(receipt1)
session.commit()
print(receipt1)

app = FastAPI()

# create docs
# http://127.0.0.1:8000/docs
# http://127.0.0.1:8000/redoc


class User(BaseModel):
    name: str
    last_name: str
    email: str
    gender: None | str


@app.get("/")
def home():
    return {"message": "Hello World"}
    # cmd uvicorn filename:app --reload
    # reload see file changes


@app.get("/user/{id}")
def get_user(id: int):
    return {'id': id}


@app.post("/cliente")
def put_user(user: User):
    user.gender = 'M'
    return user

# pip install jinja2 python-multipart
