"""match date field

Revision ID: fc955ab74891
Revises: 32bc1b7e9c4b
Create Date: 2023-07-06 19:35:27.672051

"""
from alembic import op
import sqlalchemy as sa

from src.domain.v1.team_management.matches import MatchesModel

# revision identifiers, used by Alembic.
revision = 'fc955ab74891'
down_revision = '32bc1b7e9c4b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        MatchesModel.__tablename__,
        sa.Column('match_date', sa.DateTime, nullable=True))


def downgrade() -> None:
    op.drop_column(
        MatchesModel.__tablename__,
        "match_date"
    )
