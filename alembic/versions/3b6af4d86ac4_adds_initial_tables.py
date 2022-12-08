"""Adds initial tables

Revision ID: 3b6af4d86ac4
Revises:
Create Date: 2022-12-08 12:12:43.711237

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "3b6af4d86ac4"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "cliente",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("nome", sa.String(length=50), nullable=False),
        sa.Column("email", sa.String(length=50), nullable=False),
        sa.Column("telefone", sa.String(length=11), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
    )
    op.create_table(
        "pet",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=50), nullable=False),
        sa.Column("especie", sa.String(length=50), nullable=False),
        sa.Column("raca", sa.String(length=50), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "servico",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("preco", sa.Numeric(precision=8, scale=2), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade() -> None:
    op.drop_table("servico")
    op.drop_table("pet")
    op.drop_table("cliente")
