# Autoparts Shop MVP

A simple Django-based web application that demonstrates a product catalog with search, sorting, tag filtering, pagination and basic analytics.  
The project was built as a learning and portfolio project with focus on backend logic, data flow and production setup.

Live demo: https://autoparts-shop-mvp.onrender.com/

---

## Features

- Product catalog with pagination
- Text search by product title
- Sorting (default, price ascending, price descending)
- Tag-based filtering (Many-to-Many relationship)
- Responsive layout using Bootstrap
- Product detail page
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

---

## Project Structure
```
autoparts_shop_mvp/
├── apps/
│   └── catalog/          # Django app: product catalog
│
├── fixtures/
│   └── initial_data.json # initial database data (fixtures)
├── manage.py
├── requirements.txt
└── README.md
```
---

## Search, Sorting and Filtering

- Search is implemented using `icontains` on product titles
- Sorting is controlled via GET parameters
- Tag filtering uses an explicit Many-to-Many table
- All GET parameters are preserved across pagination and navigation

---

## Visit Logging

A custom Django middleware logs page visits:
- URL path
- Client IP address
- Timestamp

Static files and admin pages are excluded.  
All records can be viewed through Django admin.

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

## Notes

This project is intentionally kept simple and focused on backend fundamentals:
* clear data relationships
* predictable request handling
* production-aware configuration
* It is not intended to be a full e-commerce solution.

--- 

##  Contact

Author: Igor Iaroshevych  
GitHub: https://github.com/Igor-prog41

