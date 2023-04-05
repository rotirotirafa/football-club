"""teste criando roles table

Revision ID: c73a8f364fc2
Revises: 
Create Date: 2023-04-03 16:14:17.621077

"""
from alembic import op
import sqlalchemy as sa

from src.domain.v1.roles.model import RolesModel


# revision identifiers, used by Alembic.
revision = 'c73a8f364fc2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        RolesModel.__tablename__,
        sa.Column("role_id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String(45), nullable=False)
    )
    


def downgrade() -> None:
    op.drop_table(RolesModel.__tablename__)
