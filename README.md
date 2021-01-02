# FinanceMe Backend 💸

This is the backend for the FinanceMe app.

FinanceMe is an app that allows you to manage your finances, simply. Instead of looking at excel sheets of your monthly statements, this app helps you visualize it a lot nicer.

## Data Model 💽

Every model has two attributes:

- id: uniqueidentifier
- created_at: datetime

### Models

- Charge: a recurring charge the user will make (form of debit)
  - date: date
  - description: string
  - price_amount: number
  - account: string
- Purchase: a purchase the user will make (form of debit)
  - date: date
  - description: string
  - price_amount: number
  - buy_link: string
  - account: string
- Earning: am earning the user will gain (form of credit)
  - date: date
  - description: string
  - price_amount: number
  - account: string

### Other

- Some of these models happen in the future (i.e. future purchases, future pay checks, etc.) but they are regardless a purchase or pay check model

## Technologies 🎷

- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
- [PostgreSQL](https://www.postgresql.org/)
- [Docker](https://www.docker.com/)

## Commands ⭕

### Local (this will not work after adding SQLAlchemy (check [here](#issues-running-locally)))

1. Install virtual environment: `virtualenv venv`
2. Enable virtual environment: `source venv/Scripts/activate`
3. Install all dependencies: `pip install -r src/requirements.txt`
4. Create FLASK_APP environment variable: `export FLASK_APP=src/project/__init__.py`
5. Run flask app: `flask run`
   - To run a different port, it would be: `flask run -h localhost -p 8000`

### Docker

1. Build and spin up containers: `docker-compose up -d --build` (combo of `docker-compose build` and `docker-compose up -d`)
2. Create table(s): `docker-compose exec web python manage.py create_db`

#### Other

- Kill and remove docker container: `docker-compose down -v` (**deletes and removes everything from db**)
- Seed database: `docker-compose exec web python manage.py seed_db`
- Enter table: `docker-compose exec db psql --username=sam --dbname=financeme_db`

### Postgres

- Connect to database: `\c financeme_db` (**must do this in order to query anything within db**)

## Resources 💨

- [Create a React + Flask Project](https://www.youtube.com/watch?v=Q2eafQYgglM)
- [Modular Applications with Blueprints](https://flask.palletsprojects.com/en/1.1.x/blueprints/#my-first-blueprint)
- [Dockerizing Flask with Postgres, Gunicorn, and Nginx](https://testdriven.io/blog/dockerizing-flask-with-postgres-gunicorn-and-nginx/) (_stopped at Gunicorn_)
- [SQLAlchemy Column and Data Types](https://docs.sqlalchemy.org/en/13/core/type_basics.html)

### Stackoverflow

- [Why can't I change the host and port that my Flask app runs on?](https://stackoverflow.com/a/41940807)
- [Redirecting to URL in Flask](https://stackoverflow.com/a/14343957)
- [Add a prefix to all Flask routes](https://stackoverflow.com/a/18969161)
- [Flask-SQLAlchemy import/context issue](https://stackoverflow.com/a/9695045)

## Other 🕵️‍♂️

### Issues running locally

- I started receiving issues running locally once I added in the SQLAlchemy dependency, specifically on the line where I initialize the app within the db: `db.init_app(app)`.
- Any time I tried to run locally (using something like `flask run`), I would get the error: `TypeError: can't apply this **setattr** to DefaultMeta object`.
- This can all be explained here: [https://github.com/pallets/flask-sqlalchemy/issues/852](https://github.com/pallets/flask-sqlalchemy/issues/852)
- In short, python 3.8.4 had an update that caused this to happen. Which is why Docker has no issue running this because we have the `python:3.8.1-slim-buster` base image.

## Todo ☑️

- need to think about models and how they are organized (do I really need a purchase and a transaction?)
