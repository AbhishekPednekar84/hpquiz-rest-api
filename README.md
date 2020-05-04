# [Yet Another Harry Potter Quiz](https://yahpq.rocks) (Backend)

[![Build Status](https://travis-ci.org/AbhishekPednekar84/hpquiz-rest-api.svg?branch=master)](https://travis-ci.org/AbhishekPednekar84/hpquiz-rest-api)

This repository contains the `Django` backend code for the **[yahpq.rocks](https://yahpq.rocks)** website. 

**Versions**<br/>
1. Python- v3.7
2. Django - v3.0.5
3. Django REST Framework - v3.11.0

## Creating a local setup

### Initial setup
1. Clone the repository using `git clone https://github.com/AbhishekPednekar84/hpquiz-rest-api`
2. Create a virtual environment with `python -m venv venv`
3. Activate the virtual environment with `venv\Scripts\activate` (Windows) or `source venv/bin/activate` (Linux / OsX)
3. Install the project dependencies using the command `pip install -r requirements.txt`

### Database setup
The project uses a `PostgreSQL` database with the connection string details stored in a `.env` file

1. Create a `.env` file in the project root folder and add the `SECRET_KEY` and the database specific environment variables (please refer to the `.env.example` file). If using another database engine, modify the details accordingly.
2. `cd` to the `quiz_api_manager` directory
3. Create a migration using the command `python manage.py makemigrations`
4. Run the migration with `python manage.py migrate`
5. Create a superuser by running `python manage.py createsuperuser`
6. Run the application using `python manage.py runserver`
7. Assuming that the application is running on the default port `8000`, the `Swagger` documentation should now be visible at `http:\\localhost:8000`

### Other setup
The project uses the `django-cors-headers` library to talk to the `Reactjs` frontend. 

1. If the frontend is running on a port other than `3000`, modify the `CORS_ORIGIN_WHITELIST` property in `settings.py`
2. Add data using the `django shell` or via https:\\localhost:8000\admin
---
## Running tests
The project uses the `pytest-django` library to run test cases. To run a test, `cd` to the `quiz_api_manager` directory and run the `pytest` command
