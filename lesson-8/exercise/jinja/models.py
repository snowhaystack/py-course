from database import Base
from sqlalchemy.orm import relationship
import sqlalchemy as db
# create mapping table for user


class User(Base):
    __tablename__ = "username_tracking"
    id = db.Column("id", db.Integer, primary_key=True, autoincrement=True)
    name = db.Column("name", db.Text)
    last_name = db.Column("last_name", db.Text)
    email = db.Column("email", db.Text)
    pwds = relationship("Pwd", back_populates="users")

    def __str__(self) -> str:  # for print result
        return f"({self.id}) last_name: {self.last_name} -- name {self.name} -- pwds {self.pwds}"

    def __repr__(self):
        return f"({self.id}) last_name: {self.last_name} -- name {self.name} -- pwds {self.pwds}"

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
