from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Charge(db.Model):
    __tablename__ = "charges"

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, nullable=False)
    date = db.Column(db.Date, nullable=False)
    description = db.Column(db.String(128), nullable=False)
    price_amount = db.Column(db.Integer, nullable=False)
    account = db.Column(db.String(128), nullable=False)

    def __init__(self, date, description, price_amount, account):
        self.created_at = datetime.now()
        self.date = date
        self.description = description
        self.price_amount = price_amount
        self.account = account