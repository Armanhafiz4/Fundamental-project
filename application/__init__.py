from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:root@34.89.81.100/flask_db"
app.config["SECRET_KEY"] = "Naima"

db = SQLAlchemy(app)

from application import routes 