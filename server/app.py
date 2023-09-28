from setup import app
from flask_restful import Resource, Api
from models import Book, Author
from flask import jsonify,make_response

api = Api(app)
@app.route('/')
def home():
    return {"hello":"Welcome to my api"}

class Books(Resource):
    def get(self):
        books = [book.to_dict() for book in Book.query.all()]
        return books,200
    
class Authors(Resource):
    def get(self):
        authors = [author.to_dict() for author in Author.query.all()]
        return authors,200

api.add_resource(Authors,'/authors')
api.add_resource(Books,'/books')

if __name__ == '__main__':
    app.run()
