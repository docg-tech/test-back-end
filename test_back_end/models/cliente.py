import sqlalchemy as sa

from . import db


class Cliente(db.Model):
    __tablename__ = "cliente"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    telefone = db.Column(db.String(11), nullable=False)
    # TODO: Column Pets
