from setup import app
from flask_restful import Resource, Api
from models import Book, Author, db, User
from flask import jsonify,make_response, request, abort, session

api = Api(app)
@app.before_request
def check_if_logged_in():  
    session['new_id'] = "random string"
    print(session) 
    if not session['user2_id'] and request.endpoint != 'sign_up' :
        return {'error': 'Unauthorized'}, 401
@app.route('/')
def home():
    return {"hello":"Welcome to my api"}

class Books(Resource):
    def get(self):
        books = [book.to_dict() for book in Book.query.all()]
        return books,200
    
    def post(self):
        data = request.get_json()
        bookname = data['name']
        authorname = data['authorname']
        # bookname = request.form.get('name')
        # authorname = request.form.get('authorname')

        author = Author.query.filter_by(name=authorname).first()
        if author:
            bookauthor = author.id
        else:
            newauthor = Author(name=authorname)
            db.session.add(newauthor)
            db.session.commit()
            bookauthor = newauthor.id
        newbook = Book(name=bookname, author_id=bookauthor)
        try:
            db.session.add(newbook)
            db.session.commit()
            return {"message": "New Book successfully added"}
        except:
            abort(422, "Couldn't save book")
            
        return {'message': "Book could not be added"}




    
class Authors(Resource):
    def get(self):
        authors = [author.to_dict() for author in Author.query.all()]
        return authors,200
    

class SignUp(Resource):
    def post(self):
        print("here")
        data = request.get_json()
        username = data['username']
        password = data['password']

        if username and password:

            new_user = User(username=username)
            new_user.password_hash=password
            try:
                print(new_user)
                db.session.add(new_user)
                db.session.commit()
                session['user2_id'] = new_user.id
                print("Done")
            except Exception as e:
                return{"error": str(e)}
                
            #     abort(422, description="Username is already taken")
            # session['user2_id'] = new_user.id
            # session['new_sesh'] = new_user.username
            # print(session.get_item('userxx_id'))

            return{"message":"New User Created"}
        
        return {'message': "No username or password"}
    
    def get(self):
        users = [user.to_dict() for user in User.query.all()]
        return users, 200
    

class Login(Resource):
    def post(self):
        data = request.get_json()
        username = data['username']
        password = data['password']

        myuser = User.query.filter_by(username=username).first()
        if myuser.authenticate(password):
            session['userxx_id'] = myuser.id
            return myuser.to_dict(),200
        
        return{"error": "Cannot be Logged in, Check Credentials"}


class CheckSession(Resource):
    def get(self):
        if session.get('user_id'):
            user = User.query.filter_by(User.id == session['user_id']).first()
            return user.to_dict,200
        return {"error":"No Sessions found"},204
    

api.add_resource(Authors,'/authors')
api.add_resource(Books,'/books')
api.add_resource(SignUp,'/signup', endpoint="sign_up")
api.add_resource(Login,'/login')
api.add_resource(CheckSession,'/checksession')

if __name__ == '__main__':
    app.run()
