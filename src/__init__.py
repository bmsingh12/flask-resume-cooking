from flask import Flask
from config import Config

import os

template_dir = os.path.abspath(os.getcwd() + '/templates')
static_dir = os.path.abspath(os.getcwd() + '/static')
app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)
app.config.from_object(Config)

from src.controller import routes

