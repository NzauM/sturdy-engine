from setup import db,app
from faker import Faker
from models import Book, Author

fake = Faker()

with app.app_context():
    Book.query.delete()
    Author.query.delete()

    authors = []
    for i in range(20):
        author = Author(name=fake.name())
        authors.append(author)
    db.session.add_all(authors)
    db.session.commit()
    print("Authors Seeded")

    books = []
    for i in range (1,21):
        book = Book(name=fake.name(), author_id=i)
        books.append(book)
    db.session.add_all(books)
    db.session.commit()
    print("Books seeded")

