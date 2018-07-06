#coding:utf8
from flask_sqlalchemy import SQLAlchemy
import logging as lg
from .views import app
import enum

#create database connection object

db = SQLAlchemy(app)

class Gender(enum.Enum):
    female = 0
    male = 1
    other = 2


class Content(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=False)
    gender = db.Column(db.Enum(Gender), nullable=False)

    def __init__(self, description, gender):
        self.description = description
        self.gender = gender

def init_db():
    db.drop_all()
    db.create_all()
    db.session.add(Content(u"THIS IS SPARTAAAAAAA!!!", Gender['male']))
    db.session.add(Content(u"What's your favorite scary movie?", Gender['female']))
    db.session.add(Content(u"Personne ne te faisait pitié, ni sur le moment, ni après, on était absolument sans défense devant toi.", Gender['male']))
    db.session.commit()
    lg.warning('Database initialized!')

