# SQLAchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sqlalchemy as db
import datetime
import random
from rich.console import Console

console = Console()

Base = declarative_base()
DB_CONN = "sqlite:///./core.db"


def get_random_pwd(num):
    def load_pwwd():
        PWD_STACK = 'bf.txt'
        with open(PWD_STACK, 'r') as file_in:
            # pwd = [line.replace("\n","") for line in file_in.readlines()] #all
            pwd = [str(file_in.readline()).replace("\n", "")
                   for i in range(1, num)]
        return pwd

    all_pwd = load_pwwd()
    sng_pwd = random.choice(all_pwd)
    new_pwd = Pwd()
    new_pwd.value = sng_pwd
    new_pwd.attempt_r = random.randint(57, 50000)
    new_pwd.data = datetime.date(
        2023, random.randint(1, 12), random.randint(1, 28))
    return new_pwd

# create mapping table for receipt


class Pwd(Base):
    __tablename__ = "bf_tracking"
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    value = db.Column('value', db.Text)
    attempt_r = db.Column('attempt_r', db.Integer)
    data = db.Column('date', db.Date)

    def __str__(self) -> str:  # for print result
        return f"({self.id}) pwd: {self.value} -- date {self.data} -- rmd_val {self.attempt_r}"

    def __repr__(self):
        return f"({self.id}) pwd: {self.value} -- date {self.data} -- rmd_val {self.attempt_r}"


# init db connection
engine = db.create_engine(DB_CONN, echo=True)
# create tables
Base.metadata.create_all(engine)
# session init
Session = sessionmaker(bind=engine)
session = Session()
# -----------
pwd = get_random_pwd(100)
console.log(pwd)
# -----------
session.add(pwd)
session.commit()
result = session.query(Pwd).all()
console.log(result)
