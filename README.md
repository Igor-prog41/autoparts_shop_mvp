# Autoparts Shop MVP (Django Backend Project)

Backend-focused e-commerce MVP built with Django, designed to
demonstrate real-world backend architecture, containerization, and
production-ready practices.

Live demo:\
https://autoparts-shop-mvp.onrender.com/

------------------------------------------------------------------------

##  Overview

This project simulates a simplified online store backend with:

-   product catalog
-   cart system (guest + authenticated users)
-   authentication (session + JWT)
-   REST API
-   production-like environment using Docker and PostgreSQL

The focus is on **backend engineering practices**, not UI.

------------------------------------------------------------------------

##  Tech Stack

-   Python 3.12\
-   Django 4.2\
-   Django REST Framework\
-   PostgreSQL (Docker / production)\
-   Docker & Docker Compose\
-   Gunicorn\
-   Whitenoise\
-   Render (deployment)\
-   GitHub Actions (CI)

------------------------------------------------------------------------

##  Docker Setup (Production-like)

The application is fully containerized:

-   `web` → Django + Gunicorn\
-   `db` → PostgreSQL

Docker Compose orchestrates both services in a shared network.

------------------------------------------------------------------------

## ️ Environment Configuration

DATABASE_URL=postgres://user:password@db:5432/shop\
ENV=production

``` python
ENV = os.getenv("ENV", "development").lower()
DEBUG = ENV != "production"
```

------------------------------------------------------------------------

## Architecture

-   Views --- HTTP & API endpoints\
-   Service layer --- business logic\
-   Models (ORM) --- data layer

------------------------------------------------------------------------

##  Features

-   Product catalog (pagination, search, filtering)
-   Cart system (guest + user)
-   Authentication (session + JWT)
-   REST API
-   Middleware logging

------------------------------------------------------------------------

##  Author

Igor Iaroshevych\
Canada (Alberta)\
https://github.com/Igor-prog41
