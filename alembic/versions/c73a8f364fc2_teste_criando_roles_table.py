"""teste criando roles table

Revision ID: c73a8f364fc2
Revises: 
Create Date: 2023-04-03 16:14:17.621077

"""
from alembic import op
import sqlalchemy as sa

from src.models.roles import Roles


# revision identifiers, used by Alembic.
revision = 'c73a8f364fc2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        Roles.__tablename__,
        sa.Column("role_id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String(45), nullable=False)
    )
    


def downgrade() -> None:
    op.drop_table(Roles.__tablename__)
