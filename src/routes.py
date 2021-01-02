from flask import Blueprint

api = Blueprint('api', __name__)

@api.route('/')
def index():
    return "finance me api"

@api.route('/transactions')
def transactions():
    return "transactions"

@api.route('/transactions/upload')
def upload_transactions():
    return "upload"