# Autoparts Shop MVP (Django Backend Portfolio Project)

A Django-based backend-focused MVP demonstrating production-oriented architecture,
authentication flows, shopping cart logic, and REST API design.

Built as a portfolio project with emphasis on:
- clean backend architecture
- separation of concerns
- real-world data flow

Live demo: https://autoparts-shop-mvp.onrender.com/

---

## Features

- Product catalog with pagination, search, sorting and tag filtering
- Session-based cart for guest users
- User cart with automatic cart merge on login/registration
- Authentication system:
  - Session authentication (HTML)
  - JWT authentication (API)
- REST API for authentication and cart operations
- Service layer for business logic
- Django admin panel
- Page visit logging via custom middleware
- PostgreSQL in production, SQLite for local development
- Environment-based configuration (.env)

---

## Tech Stack

- Python 3
- Django 4.2
- PostgreSQL (production)
- SQLite (local development)
- Bootstrap 5
- Whitenoise (static files)
- Render (deployment)
- Django REST Framework
- SimpleJWT (JWT authentication)

---

## Architecture Overview

The project follows a layered architecture:

- HTTP views for server-rendered pages
- API views for JSON-based access
- Service layer for shared business logic
- Django ORM as data layer

---

## Project Structure
```
autoparts_shop_mvp/
├── apps/
│   ├── catalog/          # Django app: product catalog
│   ├── users/     # Authentication (HTML + API)
│   └──cart/      # Cart logic (guest + user)
│
├── fixtures/
│   └── initial_data.json # initial database data (fixtures)
├── manage.py
├── requirements.txt
└── README.md
```
---

## Authentication

- HTML: session-based authentication
- API: JWT-based authentication (access + refresh)
- Guest carts are merged into user carts on login or registration

---

## API Endpoints (examples)

POST /api/register/
POST /api/login/
GET  /api/cart/

---

## Search, Sorting and Filtering

- Search is implemented using `icontains` on product titles
- Sorting is controlled via GET parameters
- Tag filtering uses an explicit Many-to-Many table
- All GET parameters are preserved across pagination and navigation
- Implemented using Django ORM and query optimization patterns

---

## Visit Logging

A custom Django middleware logs page visits:
- URL path
- Client IP address
- Timestamp

Static files and admin pages are excluded.  
All records can be viewed through Django admin.
Demonstrates custom middleware and request lifecycle understanding.

---

## Environment Variables

The project uses environment variables for sensitive configuration:

SECRET_KEY
DATABASE_URL
CLOUDINARY_API_KEY
CLOUDINARY_API_SECRET
CLOUDINARY_CLOUD_NAME

A `.env` file is used locally and excluded from version control.

---

## Local Setup

1. Clone the repository
2. Create and activate virtual environment
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
4. Create .env file
5. Run migrations:
     ```bash
    python manage.py migrate
6. Create admin user:
    ```bash
   python manage.py createsuperuser
7. Run development server:
    ```bash
   python manage.py runserver
   
---

## Admin Panel

Django admin is available at:

/admin/
It is used to:

View logged page visits

---

## Roadmap

- Order and payment flow (test mode)
- Automated tests
- Dockerization

---

## Notes

This project is intentionally kept simple and focused on backend fundamentals:
* clear data relationships
* predictable request handling
* production-aware configuration
* It is not intended to be a full e-commerce solution.

--- 

##  Contact

Author: Igor Iaroshevych  
Location: Canada (Alberta)
GitHub: https://github.com/Igor-prog41

