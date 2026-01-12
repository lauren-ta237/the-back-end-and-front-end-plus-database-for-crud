# Full-Stack CRUD Application

## Overview

This project is a full-stack CRUD (Create, Read, Update, Delete) application built with a clear separation between frontend, backend, and database layers.

- **Frontend**: A user interface for interacting with the system  
- **Backend**: A FastAPI-powered REST API that handles business logic and database operations  
- **Database**: SQL-based storage for persistent data (MySQL)

The application allows users to perform CRUD operations seamlessly through the UI, with FastAPI managing requests and responses between the frontend and backend.

---

## Features

- User-friendly frontend UI for CRUD operations  
- FastAPI backend with modular routes and controllers  
- MySQL database integration using SQLAlchemy  
- RESTful API endpoints for data management  
- Clear separation of concerns between frontend and backend  

---

## Technologies Used

### Frontend
- HTML  
- CSS  
- JavaScript  

### Backend
- FastAPI  
- Uvicorn  
- SQLAlchemy  
- Pydantic  

### Database
- MySQL  

---

## Setup Instructions

### Clone the Repository

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo


---

Backend Setup

1. Navigate to the backend directory:



cd backend

2. Create and activate a virtual environment:



python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows

3. Install dependencies:



pip install -r requirements.txt

4. Run the FastAPI server:



uvicorn main:app --reload

The backend will be available at:

http://127.0.0.1:8000

Interactive API documentation (Swagger UI):

http://127.0.0.1:8000/docs


---

Database Setup

1. Configure your database connection in backend/database.py.


2. Update the MySQL credentials:

Host

User

Password

Database name



3. Run migrations or create tables using SQLAlchemy models.




---

Frontend Setup

1. Navigate to the frontend directory:



cd frontend

2. Install dependencies (if applicable):



npm install

3. Start the frontend server:



npm start


---

Backend API Endpoints

Base URL

http://127.0.0.1:8000


---

Create a Record

POST /items/

Creates a new item in the database.

Request Body (JSON):

{
  "name": "Sample Item",
  "description": "This is a sample item"
}

Response:

{
  "id": 1,
  "name": "Sample Item",
  "description": "This is a sample item"
}


---

Get All Records

GET /items/

Fetches all items from the database.

Response:

[
  {
    "id": 1,
    "name": "Sample Item",
    "description": "This is a sample item"
  }
]


---

Get a Single Record

GET /items/{id}

Fetches a single item by ID.

Example:

GET /items/1


---

Update a Record

PUT /items/{id}

Updates an existing item.

Request Body (JSON):

{
  "name": "Updated Item",
  "description": "Updated description"
}


---

Delete a Record

DELETE /items/{id}

Deletes an item by ID.

Response:

{
  "message": "Item deleted successfully"
}


---

Notes

Test all API endpoints using Swagger UI at /docs

Ensure the backend is running before starting the frontend

Adjust endpoint names (e.g., items) based on your actual models
