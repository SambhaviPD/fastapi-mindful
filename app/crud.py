from sqlalchemy.orm import Session

from . import models, schemas

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_email(db:Session, email: str):
    return db.query(models.User).filter(models.User.email ==  email).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "dummyhash"
    db_user = models.User(email=user.email, password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_author(db: Session, author_id: int):
    return db.query(models.Author).filter(models.Author.id == author_id).first()

def get_author_by_name(db:Session, author_name: str):
    return db.query(models.Author).filter(models.Author.name.like(author_name)).all()

def get_authors(db:Session, skip: int = 0, limit: int = 100):
    return db.query(models.Author).offset(skip).limit(limit).all()

def create_author(db: Session, author: schemas.AuthorCreate):
    db_author = models.Author(name=author.name, genre=author.genre)
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author