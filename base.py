from flask import Flask, render_template, redirect
import configparser
import requests
from flask_sqlalchemy import SQLAlchemy

#Configuration File
config = configparser.ConfigParser()
config.read("config.conf")

#Flask Configuration
app = Flask(__name__)
app.config["SECRET KEY"] = config["DEFAULT"]["SECRET_KEY"]
app.config["FLASK_ENV"] = config["DEFAULT"]["FLASK_ENV"]
app.config["WTF_CSRF_ENABLED"] = True

#DB Configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///userlogins.sqlite3"
db = SQLAlchemy(app)

#DB Model
class userlogins(db.Model):
    _id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(250), unique = True)
    password = db.Columm(db.String(250), unique = True)

    def __init__(self, email, password):
        self.email = email
        self. passßword = password



#Index Route
@app.route('/', methods=["GET", "POST"])
def index():
    return 'Hello World'