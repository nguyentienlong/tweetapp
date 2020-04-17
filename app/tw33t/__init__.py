
from flask import Flask
import sys

import logging
from logging.handlers import RotatingFileHandler

app = Flask(__name__)
application = app

# Setup the app with the config.py file
app.config.from_object('config')

# Set up log handler
file_handler = RotatingFileHandler(app.config['LOG_FILE'], maxBytes=10000, backupCount=1)
file_handler.setLevel(logging.INFO)
formatter = logging.Formatter('[%(asctime)s] %(levelname)s %(pathname)s:%(lineno)d %(message)s')
file_handler.setFormatter(formatter)
app.logger.addHandler(file_handler)

from .views.main_page import main_page
app.register_blueprint(main_page)

# bind api to app
from app.tw33t.resources import api
api.init_app(app, version='1.0.0', title='api')