from flask import Flask, Blueprint, jsonify
from flask_restplus import Api
from ma import ma
from db import db

from controllers.book import Book, BookList, book_ns
from marshmallow import ValidationError

from server.instance import server

api = server.api
app = server.app



@app.before_first_request
def create_tables():
    db.create_all()


@api.errorhandler(ValidationError)
def handle_validation_error(error):
    return jsonify(error.messages), 400


api.add_resource(Book, '/books/<int:id>')
api.add_resource(BookList, '/books')
#aqui era o erro
db.init_app(app)
if __name__ == '__main__':
    ma.init_app(app)
    server.run()
