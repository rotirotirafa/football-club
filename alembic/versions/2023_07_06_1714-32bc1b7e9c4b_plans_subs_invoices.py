"""plans subs invoices

Revision ID: 32bc1b7e9c4b
Revises: 15479bd7bf3c
Create Date: 2023-07-06 17:14:41.423605

"""
from alembic import op
import sqlalchemy as sa

from src.domain.v1.management.invoices.model import InvoicesModel
from src.domain.v1.management.plans.model import PlansModel
from src.domain.v1.management.subscriptions import SubscriptionsModel

# revision identifiers, used by Alembic.
revision = '32bc1b7e9c4b'
down_revision = '15479bd7bf3c'
branch_labels = None
depends_on = None


def upgrade() -> None:

    op.create_table(
        PlansModel.__tablename__,
        sa.Column("plan_id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String(50), nullable=False),
        sa.Column("description", sa.String(500), nullable=True),
        sa.Column("price", sa.DECIMAL, nullable=False)
    )

    op.create_table(
        SubscriptionsModel.__tablename__,
        sa.Column("subscription_id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String(50), nullable=True),
        sa.Column("start_date", sa.DateTime, nullable=True),
        sa.Column("expiration_date", sa.DateTime, nullable=True),
        sa.Column("user_id", sa.Integer, nullable=False),
        sa.Column("plan_id", sa.Integer, nullable=True)
    )

    op.create_table(
        InvoicesModel.__tablename__,
        sa.Column("invoice_id", sa.Integer, primary_key=True),
        sa.Column("invoice_number", sa.String(32), nullable=False),
        sa.Column("amount", sa.DECIMAL, nullable=False),
        sa.Column("payment_status", sa.String(50), nullable=False),
        sa.Column("created_date", sa.DateTime, nullable=True),
        sa.Column("payment_date", sa.DateTime, nullable=True),
        sa.Column("subscription_id", sa.Integer, nullable=True)
    )

    op.create_foreign_key(
        'fk_subscription_users',
        'subscriptions', 'users',
        ['user_id'], ['user_id']
    )

    op.create_foreign_key(
        'fk_subscription_plans',
        'subscriptions', 'plans',
        ['plan_id'], ['plan_id']
    )

    op.create_foreign_key(
        'fk_invoice_subscription',
        'invoices', 'subscriptions',
        ['subscription_id'], ['subscription_id']
    )


def downgrade() -> None:
    op.drop_constraint('fk_subscription_users', 'subscriptions', type_='foreignkey')
    op.drop_constraint('fk_subscription_plans', 'subscriptions', type_='foreignkey')
    op.drop_constraint('fk_invoice_subscription', 'invoices', type_='foreignkey')
    op.drop_table(PlansModel.__tablename__)
    op.drop_table(InvoicesModel.__tablename__)
    op.drop_table(SubscriptionsModel.__tablename__)
