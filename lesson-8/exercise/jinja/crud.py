from sqlalchemy.orm import Session
import models
import schemas


def get_users(db: Session):
    return db.query(models.User).all()


def add_user(db: Session, user: schemas.BaseUser):
    user = db.add(user)
    db.commit()
    return user
