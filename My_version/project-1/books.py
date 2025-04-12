from fastapi import Body,FastAPI

app = FastAPI()

BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'math'},
    {'title': 'Title Seven', 'author': 'Author Two', 'category': 'math'},
    {'title': 'Title Eight', 'author': 'Author Two', 'category': 'math'},
    {'title': 'Title Eight', 'author': 'Author Two', 'category': 'math'},
{'title': 'Title Nine', 'author': 'Author Two', 'category': 'Science'}
]


# async is not needed for the FASTAPI.. because fast api add's in background
# @app.get("/")
# async def first_api():
#     return {"message": "Hello user, Welcome!"}


@app.get("/books")
async def read_all_books():
    return BOOKS


@app.get("/books/mybook")
async def read_my_favorite_book():
    return {'message': 'This is my favorite book!'}


@app.get("/books/{book_title}")
async def read_book(book_title :str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book     
    return {'message': 'Book not found!'}


@app.get("/books/")
async def read_catergory_by_Query(category: str):
    books_in_category = [book for book in BOOKS if book['category'].casefold() == category.casefold()]
    if books_in_category:
        return books_in_category
    else:
        return {'message': 'No books found in this category!'}
    

# Get all books from a specific author using path or query parameters
@app.get("/books/byauthor/")
async def read_books_by_author_path(author: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == author.casefold():
            books_to_return.append(book)
    return books_to_return
    

@app.get("/books/{book_author}/")
async def read_author_category_by_query(book_author: str,category : str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == book_author.casefold() and \
                book.get('category').casefold() == category.casefold():
            books_to_return.append(book)

    return books_to_return


@app.post("/books/create_book")
async def create_book(new_book = Body()):
    BOOKS.append(new_book)
    return {'message': 'Book Created & Added successfully!'}


@app.put("/books/update_book")
async def update_book(updated_book = Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == updated_book.get('title').casefold():
            BOOKS[i] = updated_book
            return {'message': 'Book Updated successfully!'}
    return {'message': 'Book not found!'}


@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title: str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == book_title.casefold():
            BOOKS.pop(i)
            return {'message': 'Book Deleted successfully!'}
            break
    return {'message': 'Book not found!'}