from flask import Flask

app = Flask(__name__)

# noinspection PyPep8
from app import routes
