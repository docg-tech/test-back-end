import sqlalchemy as sa

from . import Base


class Servico(Base):
    __tablename__ = "servico"
    id = sa.Column(sa.Integer, primary_key=True)
    preco = sa.Column(sa.Numeric(precision=8, scale=2))
