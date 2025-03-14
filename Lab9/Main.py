from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import requests

app = Flask(__name__)
api = Api(app)

books = [
    {"id": 1, "title": "1984", "author": "George Orwell", "year": 1949},
    {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
    {"id": 3, "title": "Brave New World", "author": "Aldous Huxley", "year": 1932}
]

class BookList(Resource):
    def get(self):
        return jsonify(books)

    def post(self):
        new_book = request.get_json()
        new_book["id"] = max(book["id"] for book in books) + 1 if books else 1
        books.append(new_book)
        return jsonify(new_book), 201


class Book(Resource):
    def get(self, id):
        book = next((book for book in books if book["id"] == id), None)
        if book:
            return jsonify(book)
        return {"error": "Book not found"}, 404

    def put(self, id):
        book = next((book for book in books if book["id"] == id), None)
        if book:
            data = request.get_json()
            book.update(data)
            return jsonify(book)
        return {"error": "Book not found"}, 404

    def delete(self, id):
        global books
        books = [book for book in books if book["id"] != id]
        return {"message": "Book deleted"}, 200


api.add_resource(BookList, '/books')
api.add_resource(Book, '/books/<int:id>')


if __name__ == '__main__':
    app.run(debug=True)A