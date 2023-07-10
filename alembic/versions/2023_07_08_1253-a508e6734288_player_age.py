"""player age

Revision ID: a508e6734288
Revises: 67eb1d6bdf72
Create Date: 2023-07-08 12:53:30.881382

"""
from alembic import op
import sqlalchemy as sa

from src.domain.v1.players.model import PlayersModel

# revision identifiers, used by Alembic.
revision = 'a508e6734288'
down_revision = '67eb1d6bdf72'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        PlayersModel.__tablename__,
        sa.Column("age", sa.Integer, nullable=True)
    )


def downgrade() -> None:
    op.drop_column(
        PlayersModel.__tablename__, "age"
    )
