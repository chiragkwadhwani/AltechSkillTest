from sqlalchemy.orm import Session
import models, schemas


def get_author_by_id(db: Session, id: int):
    return db.query(models.Author).filter(models.Author.id == id).first()

def get_author_by_name(db: Session, name: str):
    return db.query(models.Author).filter(models.Author.name == name).first()

def get_authors(db: Session):
    return db.query(models.Author).all()

def create_author(db: Session, item: schemas.AuthorBase):
    db_item = models.Author(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def update_author(db: Session, item: schemas.AuthorBase, authorid: int):
    db_item = db.query(models.Author).filter(models.Author.id == authorid).first()
    db_item.bio = item.bio
    db_item.birth_date = item.birth_date
    db.commit()
    return db.query(models.Author).filter(models.Author.id == authorid).first()

def delete_author(db: Session, authorid: int):
    db_item = db.query(models.Author).filter(models.Author.id == authorid).delete()
    db.commit()
    return {"message":"Delete Successful"}




def get_book_by_id(db: Session, id: int):
    return db.query(models.Book).filter(models.Book.id == id).first()

def get_book_by_name(db: Session, title: str):
    return db.query(models.Book).filter(models.Book.title == title).first()

def get_books(db: Session):
    return db.query(models.Book).all()

def create_book(db: Session, item: schemas.BookBase):
    db_item = models.Book(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def update_book(db: Session, item: schemas.BookBase, bookid: int):
    db_item = db.query(models.Book).filter(models.Book.id == bookid).first()
    db_item.description = item.description
    db_item.publish_date = item.publish_date
    db_item.author_id = item.author_id
    db.commit()
    return db.query(models.Book).filter(models.Book.id == bookid).first()

def delete_book(db: Session,  bookid: int):
    db_item = db.query(models.Book).filter(models.Book.id == bookid).delete()
    db.commit()
    return {"message":"Delete Successful"}
