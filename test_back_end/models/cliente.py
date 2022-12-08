import sqlalchemy as sa

from . import Base


class Cliente(Base):
    __tablename__ = "cliente"
    id = sa.Column(sa.Integer, primary_key=True)
    nome = sa.Column(sa.String(50), nullable=False)
    email = sa.Column(sa.String(50), nullable=False, unique=True)
    telefone = sa.Column(sa.String(11), nullable=False)
    # TODO: Column Pets
