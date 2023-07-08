"""subscription company option

Revision ID: 67eb1d6bdf72
Revises: ea48c5552c81
Create Date: 2023-07-08 11:23:11.297995

"""
from alembic import op
import sqlalchemy as sa

from src.domain.v1.customer.model import CustomersModel
from src.domain.v1.subscriptions.model import SubscriptionsModel

# revision identifiers, used by Alembic.
revision = '67eb1d6bdf72'
down_revision = 'ea48c5552c81'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        SubscriptionsModel.__tablename__,
        sa.Column("customer_id", sa.Integer, nullable=True)
    )

    op.create_foreign_key(
        'fk_subscriptions_customers',
        'subscriptions', 'customers',
        ['customer_id'], ['customer_id']
    )


def downgrade() -> None:
    op.drop_constraint('fk_subscriptions_customers', 'customers', type_='foreignkey')
    op.drop_column(CustomersModel.__tablename__, "customer_id")
