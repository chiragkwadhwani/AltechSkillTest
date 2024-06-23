from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# AUTHORS

@app.get("/authors/", response_model=list[schemas.Author])
def read_authors(db: Session = Depends(get_db)):
    authors = crud.get_authors(db)
    if authors:
        return authors
    else:
        raise HTTPException(status_code=200, detail="Authors List Not Found")


@app.get("/authors/{id}", response_model=schemas.Author)
def read_an_author(id: int, db: Session = Depends(get_db)):
    authors = crud.get_author_by_id(db,id=id)
    if authors:
        return authors
    else:
        raise HTTPException(status_code=200, detail="Author Not Found")


@app.post("/authors/", response_model=schemas.Author)
def create_author(author: schemas.AuthorCreate, db: Session = Depends(get_db)):
    db_user = crud.get_author_by_name(db, name=author.name)
    if db_user:
        raise HTTPException(status_code=400, detail="Author " + author.name + " already registered")
    return crud.create_author(db=db, item=author)


@app.put("/authors/{id}", response_model=schemas.Author)
def update_author(id:int, author: schemas.AuthorCreate, db: Session = Depends(get_db)):
    db_user = crud.get_author_by_id(db, id=id)
    if not db_user:
        raise HTTPException(status_code=400, detail="Author " + str(id) + " Not Found")
    data = crud.update_author(db, item=author, authorid=id)
    return data
    

@app.delete("/authors/{id}")
def delete_author(id:int, db: Session = Depends(get_db)):
    db_user = crud.get_author_by_id(db, id=id)
    if not db_user:
        raise HTTPException(status_code=400, detail="Author Not Found")
    return crud.delete_author(db, authorid=id)



# BOOKS

@app.get("/books/", response_model=list[schemas.Book])
def read_books(db: Session = Depends(get_db)):
    books = crud.get_books(db)
    if books:
        return books
    else:
        raise HTTPException(status_code=200, detail="Books List Not Found")


@app.get("/books/{id}", response_model=schemas.Book)
def read_a_book(id: int, db: Session = Depends(get_db)):
    books = crud.get_book_by_id(db,id=id)
    if books:
        return books
    else:
        raise HTTPException(status_code=200, detail="Book Not Found")


@app.post("/books/", response_model=schemas.Book)
def create_books(book: schemas.BookCreate, db: Session = Depends(get_db)):
    db_user = crud.get_book_by_name(db, title=book.title)
    if db_user:
        raise HTTPException(status_code=400, detail="Book " + book.title + " already registered")
    return crud.create_book(db=db, item=book)


@app.put("/books/{id}", response_model=schemas.Book)
def update_books(id: int, book: schemas.BookCreate, db: Session = Depends(get_db)):
    db_user = crud.get_book_by_id(db, id=id)
    if not db_user:
        raise HTTPException(status_code=400, detail="Book " + str(id) + " Not Found")
    data = crud.update_book(db=db, item=book, bookid=id)
    return data
    

@app.delete("/books/{id}")
def delete_book(id:int, db: Session = Depends(get_db)):
    db_user = crud.get_book_by_id(db, id=id)
    if not db_user:
        raise HTTPException(status_code=400, detail="Book Not Found")
    return crud.delete_book(db, bookid=id)
