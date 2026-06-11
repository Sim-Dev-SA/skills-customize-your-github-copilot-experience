# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Students will build a simple REST API using FastAPI, including endpoint creation, request validation, and in-memory data handling.

## 📝 Tasks

### 🛠️	Create Core API Endpoints

#### Description
Set up a FastAPI app and implement endpoints to manage a list of books. Start with basic read and create operations.

#### Requirements
Completed program should:

- Create a FastAPI app in `starter-code.py`
- Implement `GET /` that returns a welcome message
- Implement `GET /books` that returns all books
- Implement `POST /books` to add a new book


### 🛠️	Add Validation and Item Lookup

#### Description
Improve the API by validating input with Pydantic models and adding an endpoint to retrieve a single book by ID.

#### Requirements
Completed program should:

- Define a Pydantic model with fields: `id`, `title`, `author`, and `year`
- Validate incoming JSON in `POST /books`
- Implement `GET /books/{book_id}` to return one book
- Return a clear error message when the book ID does not exist
