from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse

app = FastAPI()
app.title = 'My book API'
app.version = "0.0.1"

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


@app.get("/books", tags=['books'])
def get_books():
    return books


@app.get("/books/{id}", tags=['books'])
def get_book(id: int):
    for item in books:
        if item["id"] == id:
            return item

    return []


@app.get("/books/", tags=['books'])
def get_books_by_category(category: str):
    books_category = []
    for item in books:
        if item["category"] == category:
            books_category.append(item)

    return books_category


@app.post("/books/", tags=['books'])
def create_book(id: int = Body(), title: str = Body(), category: str = Body(), date: str = Body()):
    books.append({
        'id': id,
        'title': title,
        'category': category,
        'date': date
    })

    return id


@app.put("/books/{id}", tags=['books'])
def update_book(id: int, title: str = Body(), category: str = Body(), date: str = Body()):
    for item in books:
        if item["id"] == id:
            item['title'] = title
            item['category'] = category
            item['date'] = date

    return books


@app.delete("/books/{id}", tags=['books'])
def delete_book(id: int):
    for item in books:
        if item["id"] == id:
           books.remove(item)

    return books;