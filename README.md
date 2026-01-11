# Autoparts Shop MVP

Django-based project demonstrating backend development practices with a focus on **working with databases in Python and Django**.

The project demonstrates:
- product catalog management
- relational database modeling (ForeignKey, ManyToMany)
- generation of initial database data via scripts
- a production-oriented workflow (GitHub → Render)

---

## 🛠 Technologies

- Python 3.12
- Django 4+
- PostgreSQL (production) / SQLite (local)
- Bootstrap (frontend)
- Cloudinary (image storage)

---

## 📁 Project Structure

```
autoparts_shop_mvp/
├── apps/
│   └── catalog/          # Django app: product catalog
├── fixtures/
│   └── initial_data.json # initial database data (fixtures)
├── manage.py
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started (Local)

### 1️⃣ Clone the repository

```bash
git clone <repo_url>
cd autoparts_shop_mvp
```

### 2️⃣ Create a virtual environment and install dependencies

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

---

## 🗄 Database Setup

### 3️⃣ Apply migrations

```bash
python manage.py migrate
```

### 4️⃣ Load initial data (fixtures)

```bash
python manage.py loaddata fixtures/initial_data.json
```

If the database already contains data:

```bash
python manage.py flush
python manage.py loaddata fixtures/initial_data.json
```

---

## 📦 Initial Data Generation

The database is populated using a **custom script** that generates records based on an existing **image catalog stored on Cloudinary**.

This approach allows:
- rebuilding the database from external assets
- keeping the repository free of binary files
- reproducing the same dataset across environments

The generated data is exported to JSON using Django fixtures.

---

## 🌍 Deployment (Render)

Typical deployment workflow:

```bash
python manage.py migrate
python manage.py loaddata fixtures/initial_data.json
```

On Render, the database is created empty, so fixtures can be loaded immediately after migrations.

---

## 🔐 What Is Not Stored in the Repository

- users and passwords
- superusers
- API keys or secrets
- real production data

Fixtures are used **only for initial database setup and demo purposes**.

---

## 🎯 Project Goal

The primary goal of this project is to **demonstrate practical work with Django, Python, and relational databases**, including:

- database schema design
- data generation and serialization
- reliable database initialization across environments

---

## 📌 Notes

- Fixtures must be encoded as **UTF-8 (no BOM)**
- `loaddata` inserts data but does not update existing records
- Use `flush` before reloading fixtures into a non-empty database

---

## 📬 Contact

Author: Igor Iaroshevych  
GitHub: https://github.com/Igor-prog41

