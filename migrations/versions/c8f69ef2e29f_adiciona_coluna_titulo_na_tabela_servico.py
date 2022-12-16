"""Adiciona coluna 'titulo' na tabela Servico

Revision ID: c8f69ef2e29f
Revises: 82cb83e4be04
Create Date: 2022-12-12 14:42:52.251384

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "c8f69ef2e29f"
down_revision = "82cb83e4be04"
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table("servico", schema=None) as batch_op:
        batch_op.add_column(
            sa.Column("titulo", sa.String(length=255), nullable=False)
        )


def downgrade():
    with op.batch_alter_table("servico", schema=None) as batch_op:
        batch_op.drop_column("titulo")
