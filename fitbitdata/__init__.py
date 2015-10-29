# -*- coding: utf-8 -*-
"""
    fitbitdata
    ~~~~~~~~~~
    Initiates the database and app

    :copyright: (c) 2015 by Saeed Abdullah.

"""

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

# Creates the app
app = Flask(__name__)

# Loads default config
from . import default_config
app.config.from_object(default_config)
app.config.from_envvar("FITBIT_DATA_SETTINGS")

# Sets up the database
db = SQLAlchemy(app)

# Register the API endpoints

from fitbitdata.application import application_blueprint
app.register_blueprint(application_blueprint)
