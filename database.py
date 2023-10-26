from sqlalchemy import func
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100))
    genre_id = db.Column(db.Integer,db.ForeignKey('genre.id'))
    created_at = db.Column(db.DateTime, default=func.now)
    is_read = db.Column(db.Boolean, default = False)

    def __repr__(self):
        return f"User(fullname={self.name!r})"


class Genre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    books = db.relationship('Book', backref='genre', lazy=True)
