from flask import Flask
from flask_restplus import Api


class Server():
    def __init__(self):
        self.app = Flask(__name__)
        self.api = Api(self.app,version=1.0,title='Dados de Obras',description='Obra API',doc='/docs')
        

        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        self.app.config['PROPAGATE_EXCEPTIONS'] = True

        self.book_ns = self.book_ns()

        super().__init__()

    def book_ns(self, ):
       return self.api.namespace(name='Books', description='book related operations', path='/')

    def run(self, ):
        self.app.run()


server = Server()
