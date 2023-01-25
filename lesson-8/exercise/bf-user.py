# SQLAchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
import sqlalchemy as db
import datetime
import random
import requests
from rich.console import Console

console = Console()

Base = declarative_base()
DB_CONN = "sqlite:///./core.db"
BF_COUNT = 100


def get_random_pwd(num):
    def load_pwwd():
        PWD_STACK = 'bf.txt'
        with open(PWD_STACK, 'r') as file_in:
            pwd = [line.replace("\n", "")
                   for line in file_in.readlines()]  # all
            # pwd = [str(file_in.readline()).replace("\n","") for i in range(1,num)]
        return pwd

    all_pwd = load_pwwd()
    sng_pwd = random.choice(all_pwd)
    new_pwd = Pwd()
    new_pwd.value = sng_pwd
    new_pwd.attempt_r = random.randint(57, 50000)
    new_pwd.data = datetime.date(
        2023, random.randint(1, 12), random.randint(1, 28))
    return new_pwd


def get_random_username():
    URL = "https://randomuser.me/api/?results={}"
    user_from_api = requests.get(URL).json(
    )["results"][0]
    new_cliente = User()
    new_cliente.name = user_from_api["name"]["first"]
    new_cliente.last_name = user_from_api["name"]["last"]
    new_cliente.email = user_from_api["email"]
    return new_cliente

# create mapping table for user


class User(Base):
    __tablename__ = "username_tracking"
    id = db.Column("id", db.Integer, primary_key=True, autoincrement=True)
    name = db.Column("name", db.Text)
    last_name = db.Column("last_name", db.Text)
    email = db.Column("email", db.Text)
    pwds = relationship("Pwd", back_populates="users")

# create mapping table for bf_tracking


class Pwd(Base):
    __tablename__ = "bf_tracking"
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    value = db.Column('value', db.Text)
    attempt_r = db.Column('attempt_r', db.Integer)
    data = db.Column('date', db.Date)
    userid = db.Column("userid", db.Integer,
                       db.ForeignKey("username_tracking.id"))
    users = relationship("User", back_populates="pwds")

    def __str__(self) -> str:  # for print result
        return f"({self.id}) pwd: {self.value} -- date {self.data} -- rmd_val {self.attempt_r}"

    def __repr__(self):
        return f"({self.id}) pwd: {self.value} -- date {self.data} -- rmd_val {self.attempt_r}"


# init db connection
engine = db.create_engine(DB_CONN, echo=True)
# create tables
Base.metadata.drop_all(engine)  # drop all table
Base.metadata.create_all(engine)
# session init
Session = sessionmaker(bind=engine)
session = Session()
# -----------
for i in range(1, BF_COUNT):
    user = get_random_username()
    session.add(user)
    session.commit()
    userid = user.id
    console.log(f"NEW USER ID -> {userid}")
    pwd = get_random_pwd(BF_COUNT)
    pwd.userid = user.id
    console.log(pwd)
    session.add(pwd)
    session.commit()
# -----------

users_db = session.query(User).all()
console.log(users_db)

pwds_db = session.query(Pwd).all()
console.log(pwds_db)
