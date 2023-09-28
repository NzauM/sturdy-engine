# from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from setup import db, bcrypt
from sqlalchemy.ext.hybrid import hybrid_property


# db = SQLAlchemy()
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

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    _password_hash = db.Column(db.String, nullable=False)

    @hybrid_property
    def password_hash(self):
        return {"error":"Password hashes can't be read"}
    
    @password_hash.setter
    def password_hash(self,password):
        passwordhasher = bcrypt.generate_password_hash(password.encode('utf-8'))
        self._password_hash = passwordhasher.decode('utf-8')
    
    def authenticate(self,password):
        return bcrypt.check_password_hash(self._password_hash, password.encode('utf-8'))
