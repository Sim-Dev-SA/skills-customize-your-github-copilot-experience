# Starter Code: Building REST APIs with FastAPI

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Book(BaseModel):
    id: int
    title: str
    author: str
    year: int


# In-memory storage for assignment practice.
books = [
    Book(id=1, title="Clean Code", author="Robert C. Martin", year=2008),
    Book(id=2, title="Python Crash Course", author="Eric Matthes", year=2019),
]


@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI Book API!"}


@app.get("/books")
def get_books():
    return books


@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")


@app.post("/books")
def create_book(book: Book):
    for existing_book in books:
        if existing_book.id == book.id:
            raise HTTPException(status_code=400, detail="Book ID already exists")

    books.append(book)
    return {"message": "Book added successfully", "book": book}


# Run with: uvicorn starter-code:app --reload
