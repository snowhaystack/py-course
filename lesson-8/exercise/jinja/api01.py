
from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import schemas
import requests
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory='./template')


class User(BaseModel):
    name: str
    last_name: str
    email: str
    gender: None | str


@app.get("/")
def home(request: Request):
    message = 'Welcome to bf control panel'
    return templates.TemplateResponse('home.html', context={'request': request, 'message': message})


@app.get("/user")
def get_user(request: Request):
    return templates.TemplateResponse('new_user.html', context={'request': request})


@app.post("/user")
def put_user(request: Request):
    form = request.form()
    # name = form['name']
    # last_name = form['last_name']
    # email = form['email']
    # user = schemas.CreateUser(
    #    name=form['name'], last_name=form['last_name'], email=form['email'])

   # user = schemas.CreateUser(
   #     {"nome": "test", "cognome": "test2", "email": "email"})
    # response = requests.post("http://127.0.0.1:8000/user", json=list(user))
    return form.name


@app.get("/users")
def get_users(request: Request):
    URL_API = "http://127.0.0.1:8000/users"
    users = requests.get(URL_API).json()
    return templates.TemplateResponse('users.html', context={'request': request, 'users': users})
