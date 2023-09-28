from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()
class Book(db.Model, SerializerMixin):
    __tablename__ = 'books'

    serialize_rules = ('-author.books',)

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'))

class Author(db.Model, SerializerMixin):
    __tablename__ = 'authors'

    serialize_rules = ('-books.author',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    books = db.relationship('Book', backref='author')