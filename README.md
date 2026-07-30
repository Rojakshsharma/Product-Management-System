# Product Management System

A full-stack Product Management System built with **React.js** and **FastAPI**, using **PostgreSQL** for data storage.

## Tech Stack

* **Frontend:** React.js
* **Backend:** Python, FastAPI
* **Database:** PostgreSQL
* **ORM:** SQLAlchemy
* **Validation:** Pydantic
* **API Documentation:** Swagger UI

## Features

* Create, read, update, and delete products
* PostgreSQL database integration
* SQLAlchemy ORM for database operations
* Pydantic for request data validation
* FastAPI Dependency Injection for database session management
* Interactive API testing with Swagger UI
* React frontend integrated with FastAPI REST APIs

## Architecture

```text
React.js
   ↓
FastAPI REST API
   ↓
Pydantic + Dependency Injection
   ↓
SQLAlchemy ORM
   ↓
PostgreSQL
```

## API Endpoints

| Method | Endpoint         | Description       |
| ------ | ---------------- | ----------------- |
| GET    | `/products`      | Get all products  |
| GET    | `/products/{id}` | Get product by ID |
| POST   | `/products`      | Create a product  |
| PUT    | `/products/{id}` | Update a product  |
| DELETE | `/products/{id}` | Delete a product  |

## Swagger

FastAPI automatically provides interactive API documentation through Swagger UI:

```text
http://127.0.0.1:8000/docs
```

## Project Structure

```text
Product-Management-System/
├── backend/
├── frontend/
├── .gitignore
└── README.md
```
