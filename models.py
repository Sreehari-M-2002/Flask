from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Student(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20),nullable=False)
    desc= db.Column(db.String(20),nullable=False)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable =False)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(60), unique=True, nullable=False)
    fname = db.Column(db.String(20), nullable=False)
    lname = db.Column(db.String(20), nullable = False)
