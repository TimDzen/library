from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from sqlalchemy.orm import relationship


db = SQLAlchemy()




class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100))
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'))
    created_at = db.Column(db.DateTime, nullable=False, default=func.now())

    def __repr__(self):
        return f"User(fullname={self.name!r})"


class Genre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    books = db.relationship('Book', backref='genre', lazy=True)