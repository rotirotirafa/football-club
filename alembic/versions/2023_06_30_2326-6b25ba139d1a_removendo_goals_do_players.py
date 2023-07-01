"""removendo goals do players

Revision ID: 6b25ba139d1a
Revises: a2f00bacc4fd
Create Date: 2023-06-30 23:26:20.111761

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6b25ba139d1a'
down_revision = 'a2f00bacc4fd'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.drop_constraint('fk_goals_player', 'players', type_='foreignkey')
    op.drop_column('players', 'goal_id')


def downgrade() -> None:
    pass
