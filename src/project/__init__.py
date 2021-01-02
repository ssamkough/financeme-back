import time
from flask import Flask
from flask_cors import CORS, cross_origin

from routes import api
from models import db

app = Flask(__name__)
app.register_blueprint(api, url_prefix='/api')
app.config.from_object("project.config.Config")
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app)
db.init_app(app)