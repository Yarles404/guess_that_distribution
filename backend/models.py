from flask_sqlalchemy import SQLAlchemy
from app import db

class Play(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    player_id = db.Column(db.String, nullable=False)
    correct_answer = db.Column(db.String, nullable=False)
    player_answer = db.Column(db.String, nullable=False)
    correct = db.Column(db.Boolean, nullable=False)

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)