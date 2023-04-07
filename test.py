from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
db = SQLAlchemy()
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
db.init_app(app)

class test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    adress = db.Column(db.String, nullable = False)
    state = db.Column(db.String, nullable = False)
    admin = db.Column(db.String, nullable = False)

with app.app_context():
   db.create_all()

