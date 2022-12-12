import sqlalchemy as sa
from sqlalchemy.orm import relationship

from . import db
from .pet import Pet


class Cliente(db.Model):
    __tablename__ = "cliente"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    telefone = db.Column(db.String(11), nullable=False)

    pets = db.relationship("Pet", back_populates="cliente")
