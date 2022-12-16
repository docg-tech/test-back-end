"""Adiciona colunas data_agendamento e pet_id na tabela Servico

Revision ID: e38eb30fe049
Revises: c8f69ef2e29f
Create Date: 2022-12-12 16:08:32.801138

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "e38eb30fe049"
down_revision = "c8f69ef2e29f"
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table("servico", schema=None) as batch_op:
        batch_op.add_column(
            sa.Column("data_agendamento", sa.DateTime(), nullable=False)
        )
        batch_op.add_column(sa.Column("pet_id", sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, "pet", ["pet_id"], ["id"])


def downgrade():
    with op.batch_alter_table("servico", schema=None) as batch_op:
        batch_op.drop_constraint(None, type_="foreignkey")
        batch_op.drop_column("pet_id")
        batch_op.drop_column("data_agendamento")
