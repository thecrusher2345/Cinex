from flask import Flask
from flask_mysqldb import MySQL
from routes.cinexrout import cinex
from utils.db import *
import os

app = Flask(__name__)

mysql = MySQL()
app=config(app)
mysql.init_app(app)
app.secret_key ='1234'
app.register_blueprint(cinex)
UPLOAD_FOLDER = os.path.join('static', 'images')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
