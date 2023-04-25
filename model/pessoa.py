from flask_restful import fields
from helpers.database import db

pessoa_fields = {
    'id':   fields.Integer,
    'nome':   fields.String,
    'email':   fields.String,
}


class Pessoa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String, nullable=False)
    senha = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)

    endereco = db.relationship("Endereco", uselist=False)

    def __init__(self, nome, senha, email, endereco):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.endereco = endereco

    def __repr__(self):
        return f'<Pessoa {self.nome}, {self.email}>'
