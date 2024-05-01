from __future__ import annotations

from datetime import datetime

from fastapi import FastAPI, Body, Path, Query
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List

from starlette.responses import JSONResponse

app = FastAPI()
app.title = 'My book API'
app.version = "0.0.1"


class Book(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=5, max_length=15)
    category: str = Field(min_length=5, max_length=15)
    date: datetime = Field()

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "title": "Titulo del libro",
                "category": "Programación",
                "date": "2021-11-12"
            }
        }


books = [
    {
        'id': 1,
        'title': 'Clean Code',
        'category': 'programación',
        'date': '2020-04-05'
    },
    {
        'id': 2,
        'title': 'Hábitos Atomicos',
        'category': 'productividad',
        'date': '2020-06-05'
    },
    {
        'id': 3,
        'title': 'Hijos de la Adversidad',
        'category': 'salud',
        'date': '2024-01-05'
    },
    {
        'id': 4,
        'title': 'El programador pragmatico',
        'category': 'programación',
        'date': '1981-04-05'
    }

]


@app.get("/", tags=['home'])
async def read_root():
    return HTMLResponse('<h1>Hello World</h1>')


@app.get("/books", tags=['books'], response_model=List[Book], status_code=200)
def get_books() -> JSONResponse:
    return JSONResponse(status_code=200, content=books)


@app.get("/books/{id}", tags=['books'], response_model=Book, status_code=200)
def get_book(id: int = Path(ge=1, le=2000)) -> list[Book]:
    for item in books:
        if item["id"] == id:
            return JSONResponse(status_code=200, content=item)

    return JSONResponse(status_code=404, content=[])


@app.get("/books/", tags=['books'], response_model=List[Book], status_code=200)
def get_books_by_category(category: str = Query(min_length=5, max_length=15)) -> list[Book]:
    books_category = []
    for item in books:
        if item["category"] == category:
            books_category.append(item)

    return JSONResponse(status_code=200, content=books_category)


@app.post("/books/", tags=['books'], response_model=dict, status_code=201)
def create_book(book: Book) -> list[Book]:
    books.append(book)
    return JSONResponse(status_code=201, content={"message": "Book created"})


@app.put("/books/{id}", tags=['books'], response_model=dict, status_code=200)
def update_book(id: int, book: Book) -> dict:
    for item in books:
        if item["id"] == id:
            item['title'] = book.title
            item['category'] = book.category
            item['date'] = book.date

    return JSONResponse(status_code=200, content={"message": "Book updated"})


@app.delete("/books/{id}", tags=['books'], response_model=dict, status_code=200)
def delete_book(id: int) -> dict:
    for item in books:
        if item["id"] == id:
           books.remove(item)

    return JSONResponse(status_code=200, content={"message": "Book deleted"})