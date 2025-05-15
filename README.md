# unhabitat-web-intern

This Django-based web application manages project data and exposes a JSON API. Due to limited resources, development was done entirely on a mobile device using GitHub Codespaces.

## Features

- CRUD operations for project records
- JSON API endpoints for project data
- Basic pagination
- Bootstrap-styled interface (partial)
- Models normalized from Excel data

## Getting Started

### Prerequisites

- Python 3.x
- Django 4.x or later
- Git
- A virtual environment manager (recommended)

### Installation

1. ***Clone the repository:***
git clone https://github.com/JemimaNaliaka/unhabitat_web_intern.git
cd unhabitat_web_intern

2. ***Create a virtual environment and activate it:***
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

3. ***Install dependencies:***
pip install -r requirements.txt

4. ***Run migrations:***
python manage.py migrate

5. ***Start the development server:***
python manage.py runserver

6. ***Access the app:***
Visit:
[https://congenial-yodel-wqj5rjwq7qj2gpg9-8000.app.github.dev/update/4/](https://congenial-yodel-wqj5rjwq7qj2gpg9-8000.app.github.dev/update/4/)

Or go to `/projects/` for the main project management interface.

## Notes

* Development was done entirely on mobile, so some UI features may be incomplete.
* Country, Org Unit, and Theme dropdowns are in progress and currently unpopulated.
* You can view and manage projects under `/projects/`.

## Author

***Jemima Naliaka***