from fastapi import FastAPI, Depends
import models
import schemas
import crud
from database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()
# session generator


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/users")
def get_users(db: Session = Depends(get_db)):
    users = crud.get_users(db)
    return users

# uvicorn api01:app --reload --port 8800 => server for display app
# uvicorn mainapi:app --reload --port 8000 => server for api
