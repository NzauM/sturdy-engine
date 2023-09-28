
from flask import Flask
from flask_migrate import Migrate
from models import db, Book, Author

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///booksapp2.db'


migrate = Migrate(app, db)
db.init_app(app)