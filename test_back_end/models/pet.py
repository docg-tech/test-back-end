import sqlalchemy as sa
from sqlalchemy.orm import relationship

from . import db


class Pet(db.Model):
    __tablename__ = "pet"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    especie = db.Column(db.String(50), nullable=False)
    raca = db.Column(db.String(50), nullable=False)

    cliente_id = db.Column(db.Integer, db.ForeignKey("cliente.id"))
    cliente = db.relationship("Cliente", back_populates="pets")
