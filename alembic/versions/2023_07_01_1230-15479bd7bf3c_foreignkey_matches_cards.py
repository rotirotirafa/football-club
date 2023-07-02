"""foreignkey matches cards

Revision ID: 15479bd7bf3c
Revises: 6b25ba139d1a
Create Date: 2023-07-01 12:30:45.174030

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '15479bd7bf3c'
down_revision = '6b25ba139d1a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_foreign_key(
        'fk_match_cards',
        'cards', 'matches',
        ['match_id'], ['match_id']
    )


def downgrade() -> None:
    # FK Cards
    op.drop_constraint('fk_match_cards', 'cards', type_='foreignkey')
