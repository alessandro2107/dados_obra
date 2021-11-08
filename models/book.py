from db import db
from typing import List


class BookModel(db.Model):
    __tablename__ = "obras"

    id = db.Column(db.Integer, primary_key=True)
    proprietario = db.Column(db.String(80), nullable=False, unique=True)
    empreiteiro = db.Column(db.String(80), nullable=False, unique=True)
    ende_obra = db.Column(db.String(80), nullable=False, unique=True)
    valor = db.Column(db.Integer, nullable=False)
    qnt_estacas = db.Column(db.Integer,nullable=False)
    profundidade = db.Column(db.Integer, nullable=False)
    data_inicio = db.Column(db.String(30), nullable=False, unique=True) 
    data_fim = db.Column(db.String(30), nullable=False, unique=True)

    def __init__(self, proprietario, empreiteiro,ende_obra,valor,qnt_estacas,profundidade,data_inicio,data_fim):
        self.proprietario = proprietario
        self.empreiteiro = empreiteiro
        self.ende_obra = ende_obra
        self.valor = valor
        self.qnt_estacas = qnt_estacas
        self.profundidade = profundidade
        self.data_inicio = data_inicio
        self.data_fim = data_fim

    def __repr__(self):
        return f""" 'OBRAkModel(proprietario={self.proprietario},empreiteiro={self.empreiteiro},ende_obra={self.ende_obra}, valor={self.valor},
                quantidades={self.qnt_estacas},profundidade={self.profundidade},data_inicio={self.data_inicio},data_fim={self.data_fim})' """

    def json(self):
        return {'proprietario': self.title, 'empreiteiro':self.empreiteiro,'ende_obra' 'valor': self.valor,
                'quantidades':self.quantidades,'profundidade':self.profundidade,'data_inicio':self.data_inicio,'data_fim':self.data_fim}

    @classmethod
    def find_by_title(cls, title) -> "BookModel":
        return cls.query.filter_by(title=title).first()

    @classmethod
    def find_by_id(cls, _id) -> "BookModel":
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_all(cls) -> List["BookModel"]:
        return cls.query.all()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
