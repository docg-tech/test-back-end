import sqlalchemy as sa

from . import db


class Servico(db.Model):
    __tablename__ = "servico"
    id = db.Column(db.Integer, primary_key=True)
    preco = db.Column(db.Numeric(precision=8, scale=2))
