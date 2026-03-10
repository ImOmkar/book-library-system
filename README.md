# Book Library Management System

A Django-based application that allows users to manage books and scrape book data from an external website.

## Features

- Add, edit, view and delete books
- Search books by title
- Filter books by category
- Role-based permissions:
  - **Super Admin** → Full CRUD access
  - **Admin** → Add / Edit books
  - **User** → View books
- Web scraping integration using BeautifulSoup
- Unit tests using pytest

The scraper fetches book data from:

http://books.toscrape.com

and stores it in the local database.

---

# Tech Stack

- Django
- SQLite
- BeautifulSoup
- Requests
- Pytest

---

# Setup Instructions

Clone the repository:

```
git clone <repo_url>
cd book-library-system
```

Create virtual environment:

```
python -m venv venv
```

Activate: Windows

```
.\venv\Scripts\activate
```

Activate: Linux/Mac

```
source venv/bin/activate
```

Install Dependencies:

```
pip install -r requirements.txt
```

Run Migrations:

```
python manage.py migrate
```

Create admin user:


```
python manage.py createsuperuser
```

Run Server:

```
python manage.py runserver
```

Open browser:
https://127.0.0.1:8000/books


# Scraping Feature

Admin users can scrape books by selecting a category from a dropdown menu.

Scraped fields include:

- Title
- Genre
- Price
- Description

The scraped data is automatically stored in the database.

---

# Running Tests

Run tests using:

```
pytest
```


