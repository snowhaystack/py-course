
from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory='./template')

# create docs
# jinja for templating
# http://127.0.0.1:8000/docs
# http://127.0.0.1:8000/redoc


class User(BaseModel):
    name: str
    last_name: str
    email: str
    gender: None | str


@app.get("/")
def home(request: Request):
    message = 'Welcome to bf control panel'
    return templates.TemplateResponse('home.html', context={'request': request, 'message': message})
    # return {"message":"Hello World"}
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
