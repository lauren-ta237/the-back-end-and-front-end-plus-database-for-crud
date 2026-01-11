Full-Stack CRUD Application
Overview

This project is a full-stack CRUD (Create, Read, Update, Delete) application built with:

Frontend: A user interface for interacting with the system

Backend: A FastAPI-powered REST API that handles business logic and database operations

Database: SQL-based storage for persistent data (MySQL)

The application allows users to perform CRUD operations seamlessly through the UI, with FastAPI managing requests and responses between the frontend and backend.
Features

User-friendly frontend UI for CRUD operations

FastAPI backend with modular routes and controllers

MySQL database integration using SQLAlchemy

RESTful API endpoints for data management

Clear separation of concerns between frontend and backend

Technologies Used

Frontend: Plain HTML / CSS / JavaScript

Backend: FastAPI

Database: MySQL

Other Tools: Uvicorn, SQLAlchemy, Pydantic

Setup Instructions
Clone the Repository
git clone https://github.com/your-username/your-repo.git
cd your-repo
Backend Setup

Navigate to the backend folder:

cd backend


Create a virtual environment:

python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows


Install dependencies:

pip install -r requirements.txt


Run the FastAPI server:

uvicorn main:app --reload


The backend will be available at:

http://127.0.0.1:8000


Interactive API documentation (Swagger UI):

http://127.0.0.1:8000/docs

Database Setup

Configure your database connection in backend/database.py

Update the MySQL credentials (host, user, password, database name)

Run migrations or create tables using SQLAlchemy models
Frontend Setup

Navigate to the frontend folder:

cd frontend


Install dependencies (if applicable):

npm install


Start the frontend server:

npm start

Backend API Endpoints

Below are the available REST API endpoints exposed by the FastAPI backend.

Base URL
http://127.0.0.1:8000

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

Get a Single Record

GET /items/{id}

Fetches a single item by ID.

Example:

GET /items/1

Update a Record

PUT /items/{id}

Updates an existing item.

Request Body (JSON):

{
  "name": "Updated Item",
  "description": "Updated description"
}

Delete a Record

DELETE /items/{id}

Deletes an item by ID.

Response:

{
  "message": "Item deleted successfully"
}
Notes

You can test all API endpoints using Swagger UI at /docs

Make sure the backend is running before starting the frontend

Adjust endpoint names (items) based on your actual models
