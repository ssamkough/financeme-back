from datetime import datetime
from flask.cli import FlaskGroup

from project import app, db
from models import Charge

cli = FlaskGroup(app)

@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

@cli.command("seed_db")
def seed_db():
    db.session.add(Charge(date=datetime.strptime("2020-01-23", '%Y-%m-%d'),description="Electric bill",price_amount=154,account="Savings"))
    db.session.commit()

if __name__ == "__main__":
    cli()