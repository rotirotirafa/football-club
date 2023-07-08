"""match winner and looser

Revision ID: ea48c5552c81
Revises: a5ff1a1232f8
Create Date: 2023-07-08 10:56:12.007178

"""
from alembic import op
import sqlalchemy as sa

from src.domain.v1.matches.model import MatchesModel

# revision identifiers, used by Alembic.
revision = 'ea48c5552c81'
down_revision = 'a5ff1a1232f8'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        MatchesModel.__tablename__,
        sa.Column('home_score', sa.Integer, nullable=True),
    )
    op.add_column(
        MatchesModel.__tablename__,
        sa.Column('away_score', sa.Integer, nullable=True),
    )


def downgrade() -> None:
    op.drop_column(
        MatchesModel.__tablename__,
        "home_score"
    )
    op.drop_column(
        MatchesModel.__tablename__,
        "away_score"
    )
