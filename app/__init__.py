from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# noinspection PyPep8
from app import routes
