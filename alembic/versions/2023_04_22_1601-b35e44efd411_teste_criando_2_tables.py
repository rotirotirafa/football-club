"""Teste criando 2 tables

Revision ID: b35e44efd411
Revises: 
Create Date: 2023-04-22 16:01:52.152052

"""
from datetime import datetime

from alembic import op
import sqlalchemy as sa

from src.domain.v1.roles.model import RolesModel
from src.domain.v1.users.model import UsersModel

# revision identifiers, used by Alembic.
revision = 'b35e44efd411'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        RolesModel.__tablename__,
        sa.Column("role_id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String(45), nullable=False)
    )

    op.create_table(
        UsersModel.__tablename__,
        sa.Column("user_id", sa.Integer, primary_key=True),
        sa.Column("role_id", sa.Integer, nullable=False),
        sa.Column("name", sa.String(length=60), nullable=False),
        sa.Column("email", sa.String(length=255), nullable=False),
        sa.Column("phone", sa.String(length=15), nullable=False),
        sa.Column("password", sa.Text, nullable=False),
        sa.Column("status", sa.String(length=30)),
        sa.Column("active", sa.Boolean, default=True, nullable=False),
        sa.Column("created_date", sa.DateTime, default=datetime.now(), nullable=True),
        sa.Column("updated_date", sa.DateTime, default=datetime.now(), nullable=True),
        sa.ForeignKeyConstraint(("role_id", ), ['roles.role_id'], ),
        sa.PrimaryKeyConstraint("user_id")
    )


def downgrade() -> None:
    op.drop_table(UsersModel.__tablename__)
    op.drop_table(RolesModel.__tablename__)
