"""adicionando Email e Phone como campos Unique para o Users

Revision ID: a2f00bacc4fd
Revises: 22f2e9043494
Create Date: 2023-06-30 14:20:26.438406

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a2f00bacc4fd'
down_revision = '22f2e9043494'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_unique_constraint('unique_users_email', table_name="users", columns=['email'])
    op.create_unique_constraint('unique_users_phone', table_name="users", columns=['phone'])


def downgrade() -> None:
    op.drop_constraint('unique_users_email', table_name="users", type_='unique')
    op.drop_constraint('unique_users_phone', table_name="users", type_='unique')
