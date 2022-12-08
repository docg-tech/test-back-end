import sqlalchemy as sa

from . import Base


class Pet(Base):
    __tablename__ = "pet"
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(50), nullable=False)
    especie = sa.Column(sa.String(50), nullable=False)
    raca = sa.Column(sa.String(50), nullable=False)
